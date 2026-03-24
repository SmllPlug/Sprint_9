import pytest
import allure


from faker import Faker
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions


from utils import config
from utils.urls import Urls
from utils.data import LOGIN_EMAIL, LOGIN_PASSWORD


from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.create_account_page import CreateAccountPage
from pages.create_recipe_page import CreateRecipePage


fake = Faker()

@pytest.fixture
@allure.title("Подключение драйвера (local / remote)")
def driver():
    if config.remote_driver:
        options = ChromeOptions()
        options.set_capability("browserName", config.BROWSER_NAME)
        options.set_capability("browserVersion", config.BROWSER_VERSION)

        options.set_capability(
            "selenoid:options",
            {
                "enableVNC": True,
                "enableVideo": False,
            }
        )
        driver = webdriver.Remote(
            command_executor=config.SELENOID_URL,
            options=options,
        )
    else:
        driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def main_page(driver):
    return MainPage(driver)

@pytest.fixture
def login_page(driver):
    return LoginPage(driver)

@pytest.fixture
def create_account_page(driver):
    return CreateAccountPage(driver)

@pytest.fixture
def create_recipe_page(driver):
    return CreateRecipePage(driver)

@pytest.fixture
def open_main_page(driver):
    driver.get(Urls.MAIN_PAGE_URL)
    return driver

@pytest.fixture
def registration_data():
    return {
        "name": fake.first_name(),
        "last_name": fake.last_name(),
        "username": f"user_{fake.unique.random_number(8)}",
        "email": fake.unique.email(),
        "password": f"Qa!{fake.random_number(6)}Zx",
    }

@pytest.fixture
def authorized_user(
    open_main_page,
    login_page,
    main_page,
):
    main_page.click_login_button()
    login_page.login_user(
        LOGIN_EMAIL,
        LOGIN_PASSWORD,
    )
    main_page.wait_for_exit_button_visible()
    return True
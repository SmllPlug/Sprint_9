import allure

from utils.urls import Urls
from pages.base_page import BasePage
from locators.create_account_page_locators import CreateAccountPageLocators
from locators.login_page_locators import LoginPageLocators


class CreateAccountPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Нажатие на кнопку "Создать аккаунт" в хедере')
    def click_on_create_account_button(self):
        self.click(CreateAccountPageLocators.HEADER_CREATE_ACCOUNT_BUTTON)

    @allure.step('Ввод имени')
    def enter_name(self, name):
        self.enter_text(CreateAccountPageLocators.NAME, name)

    @allure.step('Ввод фамилии')
    def enter_last_name(self, last_name):
        self.enter_text(CreateAccountPageLocators.LAST_NAME, last_name)

    @allure.step('Ввод имени пользователя')
    def enter_username(self, username):
        self.enter_text(CreateAccountPageLocators.USERNAME, username)

    @allure.step('Ввод почты')
    def enter_email(self, email):
        self.enter_text(CreateAccountPageLocators.EMAIL, email)

    @allure.step('Ввод пароля')
    def enter_password(self, password):
        self.enter_text(CreateAccountPageLocators.PASSWORD, password)

    @allure.step('Нажатие на кнопку "Создать аккаунт" на форме ввода данных')
    def click_on_create_account_form_button(self):
        self.click_js(CreateAccountPageLocators.CREATE_ACCOUNT_FORM_BUTTON)

    @allure.step('Создание аккаунта')
    def create_account(self, name, last_name, username, email, password):
        self.enter_name(name)
        self.enter_last_name(last_name)
        self.enter_username(username)
        self.enter_email(email)
        self.enter_password(password)
        self.click_on_create_account_form_button()
    
    @allure.step('Ожидание открытия страницы авторизации')
    def wait_for_login_page_opened(self):
        return self.wait_for_url_to_be(Urls.LOGIN_URL)
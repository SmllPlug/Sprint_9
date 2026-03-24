import allure


from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


from utils.waiters import DEFAULT_WAIT_TIME


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, DEFAULT_WAIT_TIME)

    @allure.step('Ожидание видимости элемента')
    def wait_for_element_visible(self, locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )

    @allure.step('Ожидание кликабельности элемента')
    def wait_for_element_clickable(self, locator):
        return self.wait.until(
            EC.element_to_be_clickable(locator)
        )   
    
    @allure.step('Ожидание наличия элемента в DOM')
    def wait_for_element_present(self, locator):
        return self.wait.until(
            EC.presence_of_element_located(locator)
        )

    @allure.step('Ожидание перехода по URL')
    def wait_for_url_to_be(self, url):
        return self.wait.until(
            EC.url_to_be(url)
        )

    @allure.step('JS-клик по элементу')
    def click_on_element(self, element):
        self.driver.execute_script(
            'arguments[0].click();',
            element
        )

    @allure.step('Клик по локатору')
    def click(self, locator):
        element = self.wait_for_element_clickable(locator)
        element.click()

    @allure.step('Клик по локатору через JS')
    def click_js(self, locator):
        element = self.wait_for_element_clickable(locator)
        self.click_on_element(element)

    @allure.step('Ввод текста')
    def enter_text(self, locator, text):
        element = self.wait_for_element_visible(locator)
        element.clear()
        element.send_keys(text)

    @allure.step('Отправка текста без очистки')
    def send_keys(self, locator, text):
        element = self.wait_for_element_present(locator)
        element.send_keys(text)

    @allure.step('Получение текущего URL')
    def get_current_url(self):
        return self.driver.current_url
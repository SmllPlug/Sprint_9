import allure

from utils.urls import Urls
from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Ожидание отображения формы авторизации')
    def wait_for_login_form_visible(self):
        return self.wait_for_element_visible(LoginPageLocators.LOGIN_FORM)

    @allure.step('Ввод электронной почты')
    def enter_email(self, mail):
        self.enter_text(LoginPageLocators.EMAIL, mail)

    @allure.step('Ввод пароля')
    def enter_password(self, password):
        self.enter_text(LoginPageLocators.PASSWORD, password)

    @allure.step('Нажатие на кнопку "Войти"')
    def click_on_sign_in_button(self):
        self.click(LoginPageLocators.SIGN_IN_BUTTON)

    @allure.step('Авторизация пользователя')
    def login_user(self, mail, password):
        self.enter_email(mail)
        self.enter_password(password)
        self.click_on_sign_in_button()
    
    @allure.step('Ожидание открытия главной страницы')
    def wait_for_main_page_opened(self):
        return self.wait_for_url_to_be(Urls.MAIN_PAGE_URL)
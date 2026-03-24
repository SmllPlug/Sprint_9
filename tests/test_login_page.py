import allure


from utils.urls import Urls
from utils.data import LOGIN_EMAIL, LOGIN_PASSWORD


class TestLoginPage:
    @allure.title("Проверка, что при авторизации происходит переход на главную страницу")
    def test_login_user_going_to_main_page(
        self,
        open_main_page,
        main_page,
        login_page
    ):
        main_page.click_login_button()
        login_page.login_user(LOGIN_EMAIL, LOGIN_PASSWORD)
        login_page.click_on_sign_in_button()
        login_page.wait_for_main_page_opened()
        assert login_page.get_current_url() == Urls.MAIN_PAGE_URL

    @allure.title("Проверка, что при авторизации происходит переход на главную страницу")
    def test_login_user_exit_button_visivle(
        self,
        open_main_page,
        main_page,
        login_page
    ):
        main_page.click_login_button()
        login_page.login_user(LOGIN_EMAIL, LOGIN_PASSWORD)
        login_page.click_on_sign_in_button()
        main_page.wait_for_exit_button_visible()
        assert main_page.wait_for_exit_button_visible()
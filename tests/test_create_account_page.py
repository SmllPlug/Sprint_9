import allure


from utils.urls import Urls


class TestCreateAccountPage:
    @allure.title('Проверка, что при регистрации происходит переход на страницу авторизации')
    def test_create_account_going_to_login_page(
        self,
        open_main_page,
        create_account_page,
        registration_data
    ):
        create_account_page.click_on_create_account_button()
        create_account_page.create_account(
            registration_data["name"],
            registration_data["last_name"],
            registration_data["username"],
            registration_data["email"],
            registration_data["password"]
        )
        create_account_page.wait_for_login_page_opened()
        assert create_account_page.get_current_url() == Urls.LOGIN_URL

    @allure.title('Проверка, что после регистрации отображается форма авторизации')
    def test_create_account_login_form_visible(
        self,
        open_main_page,
        create_account_page,
        login_page,
        registration_data
    ):
        create_account_page.click_on_create_account_button()
        create_account_page.create_account(
            registration_data["name"],
            registration_data["last_name"],
            registration_data["username"],
            registration_data["email"],
            registration_data["password"]
        )
        assert login_page.wait_for_login_form_visible()
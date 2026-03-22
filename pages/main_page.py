import allure


from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Ожидание отображения кнопки "Выход"')
    def wait_for_exit_button_visible(self):
        return self.wait_for_element_visible(MainPageLocators.EXIT_BUTTON)

    @allure.step('Нажатие на кнопку "Создать рецепт" на главной странице')
    def click_on_create_recipe_main_page(self):
        self.click(MainPageLocators.CREATE_RECIPES_BUTTON)

    @allure.step('Нажатие на кнопку Войти')
    def click_login_button(self):
        self.click(MainPageLocators.SIGN_IN_BUTTON)
'''
    @allure.step('Ожидание отображения карточки созданного рецепта')
    def wait_for_recipe_card_visible(self, recipe_name):
        locator = (
            MainPageLocators.RECIPE_CARD_BY_TITLE[0],
            MainPageLocators.RECIPE_CARD_BY_TITLE[1].format(recipe_name)
        )
        return self.wait_for_element_visible(locator)

    @allure.step('Проверка, что открыта первая страница')
    def wait_for_first_page_visible(self):
        return self.wait_for_element_visible(MainPageLocators.ACTIVE_FIRST_PAGE)
'''
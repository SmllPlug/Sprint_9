import allure

from utils.urls import Urls
from utils.data import (
    RECIPE_NAME,
    RECIPE_INGREDIENT_NAME,
    RECIPE_INGREDIENT_WEIGHT,
    RECIPE_TIME,
    RECIPE_DESCRIPTION,
    RECIPE_PIC_CATALOG,
)


class TestCreateRecipePage:
    @allure.title("Проверка, что после создания рецепта отображается его название")
    def test_create_recipe_going_to_main_page(
        self,
        open_main_page,
        authorized_user,
        main_page,
        create_recipe_page,
    ):
        main_page.click_on_create_recipe_main_page()
        create_recipe_page.create_recipe(
            RECIPE_NAME,
            RECIPE_INGREDIENT_NAME,
            RECIPE_INGREDIENT_WEIGHT,
            RECIPE_TIME,
            RECIPE_DESCRIPTION,
            RECIPE_PIC_CATALOG,
        )
        assert create_recipe_page.wait_for_recipe_card_name_visible(RECIPE_NAME)


    @allure.title("Проверка, что после создания рецепта отображается карточка рецепта")
    def test_create_recipe_card_visible(
        self,
        open_main_page,
        authorized_user,
        main_page,
        create_recipe_page,
    ):
        main_page.click_on_create_recipe_main_page()
        create_recipe_page.create_recipe(
            RECIPE_NAME,
            RECIPE_INGREDIENT_NAME,
            RECIPE_INGREDIENT_WEIGHT,
            RECIPE_TIME,
            RECIPE_DESCRIPTION,
            RECIPE_PIC_CATALOG,
        )
        assert create_recipe_page.wait_for_add_to_shopping_button_visible()
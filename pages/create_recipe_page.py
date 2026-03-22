import allure


from pages.base_page import BasePage
from locators.create_recipe_locators import CreateRecipeLocators


class CreateRecipePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Ввод названия рецепта')
    def enter_recipe_name(self, recipe_name):
        self.enter_text(
            CreateRecipeLocators.RECIPE_NAME,
            recipe_name
        )

    @allure.step('Ввод названия ингредиента')
    def enter_ingredient_name(self, ingredient_name):
        self.enter_text(
            CreateRecipeLocators.INGREDIENTS_NAME,
            ingredient_name
        )

    @allure.step('Выбор ингредиента из выпадающего списка')
    def click_on_ingredient_name_from_pick_list(self, ingredient_name):
        locator = (
            CreateRecipeLocators.INGREDIENTS_LIST[0],
            CreateRecipeLocators.INGREDIENTS_LIST[1].format(ingredient_name)
        )
        self.wait_for_element_visible(locator)
        self.click(locator)

    @allure.step('Ввод веса ингредиента')
    def enter_ingredient_weight(self, ingredient_weight):
        self.enter_text(CreateRecipeLocators.INGREDIENTS_WEIGHT, ingredient_weight)

    @allure.step('Нажатие на кнопку "Добавить ингредиент"')
    def click_on_add_ingredient_button(self):
        self.click_js(CreateRecipeLocators.INGREDIENTS_ADD_BUTTON)

    @allure.step('Ввод времени приготовления')
    def enter_cooking_time(self, cooking_time):
        self.enter_text(CreateRecipeLocators.COOKING_TIME,cooking_time)

    @allure.step('Ввод описания рецепта')
    def enter_recipe_description(self, recipe_description):
        self.enter_text(CreateRecipeLocators.RECIPE_DESCRIPTION,recipe_description)

    @allure.step('Загрузка фото')
    def add_photo(self, photo_path):
        self.send_keys(CreateRecipeLocators.DOWNLOAD_PHOTO,str(photo_path))

    @allure.step('Нажатие на кнопку "Создать рецепт"')
    def click_on_create_recipe_button_recipe_form(self):
        self.click(CreateRecipeLocators.CREATE_RECIPES_FORM_BUTTON)

    @allure.step('Создание рецепта')
    def create_recipe(
        self,
        recipe_name,
        ingredient_name,
        ingredient_weight,
        cooking_time,
        recipe_description,
        photo_path,
    ):
        self.enter_recipe_name(recipe_name)
        self.enter_ingredient_name(ingredient_name)
        self.click_on_ingredient_name_from_pick_list(ingredient_name)
        self.enter_ingredient_weight(ingredient_weight)
        self.click_on_add_ingredient_button()
        self.enter_cooking_time(cooking_time)
        self.enter_recipe_description(recipe_description)
        self.add_photo(photo_path)
        self.click_on_create_recipe_button_recipe_form()

    @allure.step('Ожидание отображения названия созданного рецепта')
    def wait_for_recipe_card_name_visible(self, recipe_name):
        locator = (
            CreateRecipeLocators.CREATE_RECIPE_NAME[0],
            CreateRecipeLocators.CREATE_RECIPE_NAME[1].format(recipe_name)
        )
        return self.wait_for_element_visible(locator)

    @allure.step('Ожидание отображения кнопки "Добавить в покупки"')
    def wait_for_add_to_shopping_button_visible(self):
        return self.wait_for_element_visible(CreateRecipeLocators.ADD_TO_SHOPPING_LIST_BUTTON)
from selenium.webdriver.common.by import By


class CreateRecipeLocators:
    RECIPE_NAME = (
        By.XPATH,
        '//label[.//div[normalize-space()="Название рецепта"]]//input'
    )

    INGREDIENTS_NAME = (
        By.XPATH,
        '//label[.//div[normalize-space()="Ингредиенты"]]//input'
    )

    INGREDIENTS_LIST = (
        By.XPATH,
        '//div[contains(@class,"container")]//div[normalize-space()="{}"]'
    )

    INGREDIENTS_WEIGHT = (
        By.XPATH,
        '//input[contains(@class,"ingredientsAmountValue")]'
    )

    INGREDIENTS_ADD_BUTTON = (
        By.XPATH,
        '//div[normalize-space()="Добавить ингредиент"]'
    )

    COOKING_TIME = (
        By.XPATH,
        '//label[.//div[normalize-space()="Время приготовления"]]//input'
    )

    RECIPE_DESCRIPTION = (
        By.XPATH,
        '//label[.//div[normalize-space()="Описание рецепта"]]//textarea'
    )

    DOWNLOAD_PHOTO = (
        By.XPATH,
        '//input[@type="file"]'
    )

    CREATE_RECIPES_FORM_BUTTON = (
        By.XPATH,
        '//button[normalize-space()="Создать рецепт" and not(@disabled)]'
    )

    RECIPE_CARD_BY_TITLE = (
        By.XPATH,
        '//div[contains(@class,"styles_single-card")][.//a[normalize-space()="{}"]]'
    )

    ADD_TO_SHOPPING_LIST_BUTTON =(
        By.XPATH,
        '//button[contains(normalize-space(.), "Добавить в покупки")]'
        )
    
    CREATE_RECIPE_NAME = (
        By.XPATH,
        '//h1[normalize-space()="{}"]'
        )
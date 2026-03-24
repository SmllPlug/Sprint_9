from selenium.webdriver.common.by import By


class MainPageLocators:
    EXIT_BUTTON = (
        By.XPATH,
        '//a[normalize-space()="Выход"]'
        )

    CREATE_RECIPES_BUTTON = (
        By.XPATH,
        '//a[@href="/recipes/create"]'
    )

    RECIPE_CARD_BY_TITLE = (
        By.XPATH,
        '//div[contains(@class,"card")][.//a[normalize-space()="{}"]]'
    )

    ACTIVE_FIRST_PAGE = (
        By.XPATH,
        '//div[contains(@class, "paginationItem") and normalize-space()="1"]'
    )

    SIGN_IN_BUTTON = (
        By.XPATH,
        '//a[@href="/signin"]'
        )
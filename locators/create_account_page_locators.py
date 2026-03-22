from selenium.webdriver.common.by import By


class CreateAccountPageLocators:
    HEADER_CREATE_ACCOUNT_BUTTON = (
        By.XPATH,
        '//a[@href="/signup"]'
    )

    NAME = (
        By.NAME, 
        'first_name'
        )
    LAST_NAME = (
        By.NAME,
        'last_name'
        )

    USERNAME = (
        By.NAME, 
        'username'
        )

    EMAIL= (
        By.NAME, 
        'email'
        )

    PASSWORD = (
        By.NAME,
        'password'
        )

    CREATE_ACCOUNT_FORM_BUTTON = (
        By.XPATH,
        '//button[normalize-space()="Создать аккаунт" and not(@disabled)]'
    )
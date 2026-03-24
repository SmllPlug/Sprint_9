from selenium.webdriver.common.by import By


class LoginPageLocators:
    EMAIL= (
        By.NAME, 
        'email'
        )

    PASSWORD = (
        By.NAME,
        'password'
        )

    SIGN_IN_BUTTON = (
        By.XPATH,
        '//button[normalize-space()="Войти"]'
    )

    LOGIN_FORM = (
        By.XPATH,
        '//div[contains(@class, "styles_inputLabelText") and normalize-space()="Электронная почта"]'
    )
from selenium.webdriver.common.by import By


class EbaySingInPageLocators:
    EMAIL_FIELD = (By.XPATH, '//input[@id="userid"]')
    PASSWORD_FIELD = (By.XPATH, '//input[@id="pass"]')
    CONTINUE_BUTTON = (By.XPATH, '//button[@id="signin-continue-btn"]')
    SIGN_IN_BUTTON = (By.XPATH, '//button[@id="sgnBt"]')

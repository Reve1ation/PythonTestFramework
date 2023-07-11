from selenium.webdriver.common.by import By


class GenericEbayPageLocators:
    CART_BUTTON = (By.XPATH, '//a[contains(@aria-label,"Your shopping cart")]')

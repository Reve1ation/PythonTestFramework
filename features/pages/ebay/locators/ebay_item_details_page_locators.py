from selenium.webdriver.common.by import By


class EbayItemDetailsPageLocators:
    ADD_TO_CART_BUTTON = (By.XPATH, '//span[text()="Add to cart"]')
    ITEM_OPTIONS = (By.XPATH, '//select[@id and @autocomplete]')

from selenium.webdriver.common.by import By


class GenericEbayPageLocators:
    CART_BUTTON = (By.XPATH, '//a[contains(@aria-label,"Your shopping cart")]')
    GUEST_BUTTONS = (By.XPATH, '//span[@class="gh-ug-guest"]')
    SIGNED_IN_CONTROL = (By.XPATH, '//button[@class = "gh-ua gh-control"]')
    SIGN_OUT_BUTTON = (By.XPATH, '//a[text()="Sign out"]')

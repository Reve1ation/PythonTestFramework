from selenium.webdriver.common.by import By


class EbayCartPageLocators:
    HEADER = (By.XPATH, '//h1[@data-test-id="main-title" and text()="Shopping cart"]')
    REMOVE_BUTTON = (By.XPATH, '//button[@data-test-id="cart-remove-item"]')
    REMOVE_ITEM_NOTICE = (By.XPATH, '//span[contains(text(), "was removed from your cart")]')
    CART_LINE_ITEM = (By.XPATH, '//div[@class="cart-bucket-lineitem"]')



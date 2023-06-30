import random

from features.pages.ebay.generic_ebay_page import GenericEbayPage


class EbayCartPage(GenericEbayPage):
    URL = 'https://cart.ebay.com'

    def __init__(self, context):
        super().__init__(context)

    @property
    def cart_page_header(self):
        return self.find_element(xpath='//h1[@data-test-id="main-title" and text()="Shopping cart"]')

    @property
    def remove_button(self):
        return self.find_elements(xpath='//button[@data-test-id="cart-remove-item"]')

    @property
    def removed_item_notice(self):
        return self.find_element(xpath='//span[contains(text(), "was removed from your cart")]')

    @property
    def cart_line_items(self):
        return self.find_elements(xpath='//div[@class="cart-bucket-lineitem"]')

    def load(self):
        self.driver.get(self.URL)
        return self

    def remove_first_item_from_cart(self):
        self.cart_remove_button[0].click()
        return self

    def verify_elements_present(self):
        elements_to_verify = [self.cart_page_header]

        for element in elements_to_verify:
            if not element.is_displayed():
                return False
        return True

    def remove_random_item(self):
        element_position_id = random.randrange(0, len(self.remove_button))
        self.remove_button[element_position_id].click()

    def verify_item_removed(self):
        return self.removed_item_notice.is_displayed()

    def count_items_in_the_cart(self):
        len(self.cart_line_items)

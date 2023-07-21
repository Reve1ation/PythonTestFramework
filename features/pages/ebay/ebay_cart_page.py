import random

from features.pages.ebay.locators.ebay_cart_page_locators import EbayCartPageLocators
from features.pages.ebay.generic_ebay_page import GenericEbayPage


class EbayCartPage(GenericEbayPage):
    URL = 'https://cart.ebay.com'

    def __init__(self, context):
        super().__init__(context)

    def cart_page_header(self):
        return self.find_element(EbayCartPageLocators.HEADER)

    def remove_button(self):
        return self.find_elements(EbayCartPageLocators.REMOVE_BUTTON)

    def removed_item_notice(self):
        return self.find_element(EbayCartPageLocators.REMOVE_ITEM_NOTICE)

    def cart_line_items(self):
        return self.find_elements(EbayCartPageLocators.CART_LINE_ITEM)

    def load(self):
        self.driver.get(self.URL)
        return self

    def remove_first_item_from_cart(self):
        self.remove_button()[0].click()
        return self

    def verify_elements_present(self):
        elements_to_verify = [self.cart_page_header()]

        for element in elements_to_verify:
            if not element.is_displayed():
                return False
        return True

    def remove_random_item(self):
        random.choice(self.remove_button()).click()
        return self

    def verify_item_removed(self):
        return self.removed_item_notice().is_displayed()

    def count_items_in_the_cart(self):
        len(self.cart_line_items())

from features.pages.amazon.generic_amazon_page import GenericAmazonPage
from features.pages.amazon.locators.amazon_main_page_locators import AmazonMainPageLocators
from features.pages.ebay.generic_ebay_page import GenericEbayPage
from features.pages.ebay.locators.ebay_main_page_locators import EbayMainPageLocators


class AmazonMainPage(GenericAmazonPage):
    URL = 'https://www.amazon.com/ref=nav_logo'

    def __init__(self, context):
        super().__init__(context)

    def search_input(self):
        return self.find_element(AmazonMainPageLocators.SEARCH_INPUT)

    def submit_search_button(self):
        return self.find_element(AmazonMainPageLocators.SUBMIT_SEARCH_INPUT)

    def load(self):
        self.driver.get(self.URL)
        return self

    def search_for_item(self, item):
        self.search_input().clear()
        self.search_input().send_keys(item)
        self.submit_search_button().click()

    def verify_elements_present(self):
        elements_to_verify = [self.search_input(), self.submit_search_button()]

        for element in elements_to_verify:
            if not element.is_displayed():
                return False
        return True

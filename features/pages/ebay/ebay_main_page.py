from features.pages.ebay.generic_ebay_page import GenericEbayPage
from features.pages.ebay.locators.ebay_main_page_locators import EbayMainPageLocators


class EbayMainPage(GenericEbayPage):

    URL = 'https://www.ebay.com'

    def __init__(self, context):
        super().__init__(context)

    def search_input(self):
        return self.find_element(EbayMainPageLocators.SEARCH_INPUT)

    def search_button(self):
        return self.find_element(EbayMainPageLocators.SEARCH_BUTTON)

    def sign_in_button(self):
        return self.find_element(EbayMainPageLocators.SIGN_IN_BUTTON)

    def register_button(self):
        return self.find_element(EbayMainPageLocators.REGISTER_BUTTON)

    def daily_deals_button(self):
        return self.find_element(EbayMainPageLocators.DAILY_DEALS_BUTTON)

    def brand_outlet_button(self):
        return self.find_element(EbayMainPageLocators.BRAND_OUTLET_BUTTON)

    def help_contacts_button(self):
        return self.find_element(EbayMainPageLocators.HELP_CONTACTS_BUTTON)

    def sell_button(self):
        return self.find_element(EbayMainPageLocators.SELL_BUTTON)

    def watchlist_button(self):
        return self.find_element(EbayMainPageLocators.WATCHLIST_BUTTON)

    def my_ebay_button(self):
        return self.find_element(EbayMainPageLocators.MY_EBAY_BUTTON)

    def my_ebay_list(self):
        return self.find_elements(EbayMainPageLocators.MY_EBAY_LIST)

    def shop_by_category_button(self):
        return self.find_element(EbayMainPageLocators.SHOP_BY_CATEGORY_BUTTON)

    def saved_tab(self):
        return self.find_element(EbayMainPageLocators.SAVED_TAB)

    def tabs_list(self):
        return self.find_elements(EbayMainPageLocators.TABS_LIST)

    def load(self):
        self.driver.get(self.URL)
        return self

    def navigate_to_tab_by_text(self, text):
        for element in self.tabs_list():
            if element.get_attribute("value") == text:
                return element

    def search_for_item(self, item):
        self.search_input().clear()
        self.search_input().send_keys(item)
        self.search_button().click()

    def verify_elements_present(self):
        elements_to_verify = [self.search_input(), self.search_button()]

        for element in elements_to_verify:
            if not element.is_displayed():
                return False
        return True

from features.pages.ebay.generic_ebay_page import GenericEbayPage
from features.pages.ebay.ebay_main_page_locators import EbayMainPageLocators


class EbayMainPage(GenericEbayPage):

    URL = 'https://www.ebay.com'

    def __init__(self, context):
        super().__init__(context)

    @property
    def search_input(self):
        return self.find_element(id=EbayMainPageLocators.SEARCH_INPUT.get('id'))

    @property
    def search_button(self):
        return self.find_element(xpath=EbayMainPageLocators.SEARCH_BUTTON.get('xpath'))

    @property
    def sign_in_button(self):
        return self.find_element(xpath=EbayMainPageLocators.SIGN_IN_BUTTON.get('xpath'))

    @property
    def register_button(self):
        return self.find_element(xpath=EbayMainPageLocators.REGISTER_BUTTON.get('xpath'))

    @property
    def daily_deals_button(self):
        return self.find_element(xpath=EbayMainPageLocators.DAILY_DEALS_BUTTON.get('xpath'))

    @property
    def brand_outlet_button(self):
        return self.find_element(xpath=EbayMainPageLocators.BRAND_OUTLET_BUTTON.get('xpath'))

    @property
    def help_contacts_button(self):
        return self.find_element(xpath=EbayMainPageLocators.HELP_CONTACTS_BUTTON.get('xpath'))

    @property
    def sell_button(self):
        return self.find_element(xpath=EbayMainPageLocators.SELL_BUTTON.get('xpath'))

    @property
    def watchlist_button(self):
        return self.find_element(css=EbayMainPageLocators.WATCHLIST_BUTTON.get('xpath'))

    @property
    def my_ebay_button(self):
        return self.find_element(css=EbayMainPageLocators.MY_EBAY_BUTTON.get('css'))

    @property
    def my_ebay_list(self):
        return self.find_elements(xpath=EbayMainPageLocators.MY_EBAY_LIST.get('xpath'))

    @property
    def shop_by_category_button(self):
        return self.find_element(xpath=EbayMainPageLocators.SHOP_BY_CATEGORY_BUTTON.get('xpath'))

    @property
    def saved_tab(self):
        return self.find_element(xpath=EbayMainPageLocators.SAVED_TAB.get('xpath'))

    @property
    def tabs_list(self):
        return self.find_elements(xpath=EbayMainPageLocators.TABS_LIST.get('xpath'))

    def load(self):
        self.driver.get(self.URL)
        return self

    def navigate_to_tab_by_text(self, text):
        for element in self.tabs_list:
            if element.get_attribute("value") == text:
                return element

    def verify_elements_present(self):
        pass

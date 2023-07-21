import random

from selenium.webdriver.common.by import By

from features.pages.ebay.generic_ebay_page import GenericEbayPage
from features.pages.ebay.locators.ebay_search_results_page_locators import EbaySearchResultsPageLocators


class EbaySearchResultsPage(GenericEbayPage):
    URL = 'https://www.ebay.com/n/all-categories'

    def __init__(self, context):
        super().__init__(context)

    def search_results(self):
        return self.find_elements(EbaySearchResultsPageLocators.SEARCH_RESULTS)

    def sell_type_filter_auction(self):
        return self.find_element(EbaySearchResultsPageLocators.AUCTION_FILTER)

    def sell_type_filter_buy_now(self):
        return self.find_element(EbaySearchResultsPageLocators.BUY_IT_NOW_FILTER)

    def results_contains_text(self, search_text):
        errors_counters = 0
        for index, element in enumerate(self.search_results()):
            if search_text.lower() not in element.text.lower():
                print(f"Element with mistake: {element.text}. Position = {index}")
                errors_counters += 1
        if errors_counters > 0:
            return False
        return True

    def open_random_item(self):
        element = random.choice(self.search_results())
        url = element.get_attribute('href')
        self.driver.get(url)
        return self

    def load(self):
        self.driver.get(self.URL)
        return self

    def set_ebay_filter(self, filter_name, filter_value):
        filter_locator = (EbaySearchResultsPageLocators.FILTER_BASE[0],
                          EbaySearchResultsPageLocators.FILTER_BASE[1].format(filter_name, filter_value))
        self.find_element(filter_locator).click()
        return self

    def verify_elements_present(self):
        pass

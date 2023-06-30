import random

from features.pages.ebay.generic_ebay_page import GenericEbayPage


class EbaySearchResultsPage(GenericEbayPage):
    URL = 'https://www.ebay.com/n/all-categories'

    def __init__(self, context):
        super().__init__(context)

    @property
    def search_results(self):
        return self.find_elements(xpath='//div[@id="srp-river-results"]//li[@id]//span[@role="heading"]/ancestor::a')

    @property
    def sell_type_filter_auction(self):
        return self.find_element(xpath='//ul[@class="fake-tabs__items"]//span[text()="Auction"]')

    @property
    def sell_type_filter_buy_now(self):
        return self.find_element(xpath='//ul[@class="fake-tabs__items"]//span[text()="Buy It Now"]')

    def results_contains_text(self, search_text):
        errors_counters = 0
        for index, element in enumerate(self.search_results):
            if search_text.lower() not in element.text.lower():
                errors_counters += 1
                self.logger.error(f"In the elements with index:{index} has no {search_text} in {element.text}")
        if errors_counters > 0:
            return False
        return True

    def open_random_item(self):
        element_position_id = random.randrange(0, len(self.search_results))
        element = self.search_results[element_position_id]
        url = element.get_attribute('href')
        self.driver.get(url)
        return self

    def load(self):
        self.driver.get(self.URL)
        return self

    def verify_elements_present(self):
        pass

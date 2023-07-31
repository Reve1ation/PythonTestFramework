from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from features.pages.amazon.generic_amazon_page import GenericAmazonPage
from features.pages.amazon.locators.amazon_main_page_locators import AmazonMainPageLocators
from features.pages.amazon.locators.amazon_search_results_locators import AmazonSearchResultsPageLocators
from features.pages.ebay.generic_ebay_page import GenericEbayPage
from features.pages.ebay.locators.ebay_main_page_locators import EbayMainPageLocators


class AmazonSearchResultsPage(GenericAmazonPage):

    def __init__(self, context):
        super().__init__(context)

    def search_input(self):
        return self.find_element(AmazonMainPageLocators.SEARCH_INPUT)

    def search_results_list(self):
        return self.find_elements(AmazonSearchResultsPageLocators.RESULTS)

    def filter_side_menu(self, filter_text):
        return self.find_element(
            (By.XPATH, f'//div[@id="s-refinements"]//div[@id and ./div/span[contains(text(),"{filter_text}")]]'))

    def select_side_filter_option(self, filter_text, option_text):
        self.filter_side_menu(filter_text).find_element(By.XPATH, f"//a[./span[contains(text(), '{option_text}')]]/div").click()
        return self

    def verify_item_text(self, text):
        mismatches = []
        self.wait.until(lambda x: len(self.search_results_list()) > 20)
        for element in self.search_results_list():
            if text not in element.text:
                mismatches.append(element.text)
        if len(mismatches) > 0:
            for item in mismatches:
                print(item)
                return False
        return True

    def verify_elements_present(self):
        elements_to_verify = [self.search_input()]

        for element in elements_to_verify:
            if not element.is_displayed():
                return False
        return True

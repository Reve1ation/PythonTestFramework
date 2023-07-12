import random

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from features.pages.ebay.ebay_item_details_page_locators import EbayItemDetailsPageLocators
from features.pages.ebay.generic_ebay_page import GenericEbayPage
from features.pages.widgets.add_to_cart_widget import AddToCartWidget


class EbayItemDetailsPage(GenericEbayPage):

    def __init__(self, context):
        super().__init__(context)
        self.add_to_cart_widget = AddToCartWidget(context)

    def add_to_cart_button(self):
        return self.find_element(EbayItemDetailsPageLocators.ADD_TO_CART_BUTTON)

    def item_options(self):
        return self.driver.find_elements(*EbayItemDetailsPageLocators.ITEM_OPTIONS)

    def select_random_item_options(self):
        if len(self.item_options()) > 0:
            for element in self.item_options():
                element.click()
                dropdown_option = random.choice(element.find_elements(By.XPATH, './/option[@value >=0]'))
                self.wait.until(EC.element_to_be_clickable(dropdown_option))
                dropdown_option.click()
        return self

    def verify_elements_present(self):
        pass

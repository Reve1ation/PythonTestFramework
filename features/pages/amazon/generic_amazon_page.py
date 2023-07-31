from abc import abstractmethod

from features.pages.amazon.locators.generic_amazon_page_locators import GenericAmazonPageLocators
from features.pages.ebay.locators.generic_ebay_page_locators import GenericEbayPageLocators
from features.pages.page import Page
from selenium.webdriver.support import expected_conditions as EC


class GenericAmazonPage(Page):

    def __init__(self, context):
        super().__init__(context)

    @abstractmethod
    def verify_elements_present(self):
        pass

    def element(self):
        return self.find_element(GenericAmazonPageLocators.ELEMENT)


    def verify_signed_in(self, sign_in_status):
        match sign_in_status.lower():
            case 'signed in':
                return self.user_data_button().is_displayed()
            case 'not signed in':
                return self.guest_buttons().is_displayed()
            case _:
                raise Exception(f"'{sign_in_status}' is not what is expected")

    def sign_out(self):
        self.user_data_button().click()
        self.wait.until(EC.element_to_be_clickable(self.sign_out_button()))
        self.sign_out_button().click()

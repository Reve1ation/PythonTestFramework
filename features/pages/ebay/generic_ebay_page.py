from abc import abstractmethod
from features.pages.ebay.generic_ebay_page_locators import GenericEbayPageLocators
from features.pages.page import Page


class GenericEbayPage(Page):

    def __init__(self, context):
        super().__init__(context)

    @abstractmethod
    def verify_elements_present(self):
        pass

    def cart_button(self):
        return self.find_element(GenericEbayPageLocators.CART_BUTTON)

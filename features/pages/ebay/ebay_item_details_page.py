from features.pages.ebay.ebay_item_details_page_locators import EbayItemDetailsPageLocators
from features.pages.ebay.generic_ebay_page import GenericEbayPage
from features.pages.widgets.add_to_cart_widget import AddToCartWidget


class EbayItemDetailsPage(GenericEbayPage):
    URL = 'https://www.ebay.com/n/all-categories'

    def __init__(self, context):
        super().__init__(context)
        self.add_to_cart_widget = AddToCartWidget(context)

    def add_to_cart_button(self):
        return self.find_element(EbayItemDetailsPageLocators.ADD_TO_CART_BUTTON)

    def verify_elements_present(self):
        pass

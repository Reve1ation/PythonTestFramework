from features.pages.ebay.generic_ebay_page import GenericEbayPage
from features.pages.widgets.add_to_cart_widget import AddToCartWidget


class EbayItemDetailsPage(GenericEbayPage):
    URL = 'https://www.ebay.com/n/all-categories'

    def __init__(self, context):
        super().__init__(context)
        self.add_to_cart_widget = AddToCartWidget(context)

    @property
    def add_to_cart_button(self):
        return self.find_element(xpath='//span[text()="Add to cart"]')

    def verify_elements_present(self):
        pass

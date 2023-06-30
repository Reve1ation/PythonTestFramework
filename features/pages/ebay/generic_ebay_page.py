from abc import abstractmethod

from features.pages.page import Page


class GenericEbayPage(Page):

    def __init__(self, context):
        super().__init__(context)

    @abstractmethod
    def verify_elements_present(self):
        pass

    @property
    def cart_button(self):
        return self.find_element(xpath='//a[contains(@aria-label,"Your shopping cart")]')

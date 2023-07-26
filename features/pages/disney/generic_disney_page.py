from abc import abstractmethod

from features.pages.disney.locators.generic_disney_page_locators import GenericDisneyPageLocators
from features.pages.page import Page


class GenericDisneyPage(Page):

    def __init__(self, context):
        super().__init__(context)

    @abstractmethod
    def verify_elements_present(self):
        pass

    def some_element(self):
        return self.find_element(GenericDisneyPageLocators.ELEMENT)

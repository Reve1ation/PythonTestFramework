from selenium.webdriver.common.by import By

from features.pages.disney.generic_disney_page import GenericDisneyPage
from features.pages.disney.locators.disney_second_page_locators import DisneySecondPageLocators


class DisneySecondPage(GenericDisneyPage):

    def __init__(self, context):
        super().__init__(context)

    def header_menus(self):
        return self.find_elements(DisneySecondPageLocators.DISNEY_HEADER_MENUS)

    def verify_elements_present(self):
        elements_to_verify = [self.header_menus()[0]]

        for element in elements_to_verify:
            if not element.is_displayed():
                return False
        return True

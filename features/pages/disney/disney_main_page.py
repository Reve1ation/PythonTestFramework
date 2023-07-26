from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from features.pages.disney.generic_disney_page import GenericDisneyPage
from features.pages.disney.locators.disney_main_page_locators import DisneyMainPageLocators
from selenium.webdriver.support import expected_conditions as EC


class DisneyMainPage(GenericDisneyPage):
    URL = 'https://www.disney.com'

    def __init__(self, context):
        super().__init__(context)

    def header_menus(self):
        return self.find_elements(DisneyMainPageLocators.DISNEY_HEADER_MENUS)

    def wait_for_ad_is_gone(self):
        try:
            self.driver.switch_to.frame(self.find_element(DisneyMainPageLocators.THIRD_PARTY_IFRAME))
            self.find_element(DisneyMainPageLocators.ADVERTISEMENT)
            self.driver.switch_to.default_content()
        except Exception:
            print("Ad didn't appear during expected time")
        return self

    def load(self):
        self.driver.get(self.URL)
        return self

    def open_header_menu_page(self, menu_text):
        for element in self.header_menus():
            if menu_text in element.get_attribute('text').strip():
                self.wait_for_ad_is_gone().wait.until(EC.element_to_be_clickable(element))
                element.click()
                break
        return self

    # def open_sub_menu_page(self, main_menu_text, sub_menu_text):
    #     for menu_element in self.header_menus():
    #         if main_menu_text in menu_element.get_attribute('text').strip():
    #             self.wait_for_ad_is_gone().wait.until(EC.element_to_be_clickable(menu_element))
    #             self.action.move_to_element(menu_element).perform()
    #             sub_menus_list = menu_element.find_elements(By.XPATH, '/following-sibling::div//a')
    #             for sub_menu_element in sub_menus_list:
    #                 self.wait.until(EC.element_to_be_clickable(sub_menu_element))
    #                 if sub_menu_text in sub_menu_element.get_attribute('text').strip():
    #                     sub_menu_element.click()
    #                     break
    #     return self

    def open_sub_menu_page(self, main_menu_text, sub_menu_text):
        main_menu_element = None
        for element in self.header_menus():
            if main_menu_text in element.get_attribute('text').strip():
                main_menu_element = element
                break

        if main_menu_element is None:
            raise Exception(f"Main menu item with text '{main_menu_text}' not found")

        self.wait_for_ad_is_gone().wait.until(EC.element_to_be_clickable(main_menu_element))
        self.action.move_to_element(main_menu_element).perform()

        sub_menus_list = main_menu_element.find_elements(By.XPATH, 'following-sibling::div//a')
        for sub_menu_element in sub_menus_list:
            self.wait.until(EC.element_to_be_clickable(sub_menu_element))
            if sub_menu_text in sub_menu_element.get_attribute('text').strip():
                sub_menu_element.click()
                return self

        raise Exception(f"Sub menu item with text '{sub_menu_text}' not found")

    def verify_elements_present(self):
        elements_to_verify = [self.header_menus()[0]]

        for element in elements_to_verify:
            if not element.is_displayed():
                return False
        return True

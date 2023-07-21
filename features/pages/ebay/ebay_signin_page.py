from features.pages.ebay.locators.ebay_signin_page_locators import EbaySingInPageLocators
from features.pages.ebay.generic_ebay_page import GenericEbayPage
from selenium.webdriver.support import expected_conditions as EC


class EbaySingInPage(GenericEbayPage):
    URL = 'https://signin.ebay.com'

    def __init__(self, context):
        super().__init__(context)
        self.context = context

    def email_field(self):
        return self.find_element(EbaySingInPageLocators.EMAIL_FIELD)

    def password_field(self):
        return self.find_element(EbaySingInPageLocators.PASSWORD_FIELD)

    def continue_button(self):
        return self.find_element(EbaySingInPageLocators.CONTINUE_BUTTON)

    def sign_in_button(self):
        return self.find_element(EbaySingInPageLocators.SIGN_IN_BUTTON)

    def load(self):
        self.driver.get(self.URL)
        return self

    def verify_elements_present(self):
        elements_to_verify = [self.email_field(), self.continue_button()]

        for element in elements_to_verify:
            if not element.is_displayed():
                return False
        return True

    def sign_in_as(self, user_name):
        user = '_'.join(word.lower() for word in user_name.split())
        email = self.context.user_data['users'][user]['email']
        password = self.context.user_data['users'][user]['password']
        self.email_field().send_keys(email)
        self.continue_button().click()
        self.wait.until(EC.element_to_be_clickable(self.password_field()))
        self.password_field().send_keys(password)
        self.sign_in_button().click()


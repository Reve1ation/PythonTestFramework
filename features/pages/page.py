from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Page:
    TIMEOUT = 30

    def __init__(self, context):
        self.driver = context.driver
        self.wait = WebDriverWait(context.driver, self.TIMEOUT)

    def find_element(self, locator: tuple, message=""):
        return self.wait.until(EC.presence_of_element_located(locator),
                               message=message if message else 'Element not found')

    def find_elements(self, locator: tuple, message=""):
        return self.wait.until(EC.presence_of_all_elements_located(locator),
                               message=message if message else 'Elements not found')

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging


class Page:
    TIMEOUT = 30

    def __init__(self, context):
        self.driver = context.driver
        self.wait = WebDriverWait(context.driver, self.TIMEOUT)

        logging.basicConfig(format='%(process)d-%(levelname)s-%(message)s', level=logging.DEBUG)
        c_handler = logging.StreamHandler()
        f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        c_handler.setFormatter(f_format)
        self.logger = logging.getLogger(__name__)
        self.logger.addHandler(c_handler)

    def find_element(self, **kwargs):
        strategy = list(kwargs.keys())[0].upper()
        locator = kwargs.get(list(kwargs.keys())[0])
        try:
            return self.wait.until(EC.presence_of_element_located((getattr(By, strategy), locator)))
        except Exception as e:
            self.logger.error('Element not found in the driver')
            raise e

    def find_elements(self, **kwargs):
        strategy = list(kwargs.keys())[0].upper()
        locator = kwargs.get(list(kwargs.keys())[0])
        try:
            return self.wait.until(EC.presence_of_all_elements_located((getattr(By, strategy), locator)))
        except Exception as e:
            self.logger.error('Elements not found in the driver')
            raise e

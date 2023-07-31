from selenium.webdriver.common.by import By


class AmazonMainPageLocators:
    SEARCH_INPUT = (By.XPATH, '//input[@placeholder="Search Amazon"]')
    SUBMIT_SEARCH_INPUT = (By.XPATH, '//input[@id="nav-search-submit-button"]')

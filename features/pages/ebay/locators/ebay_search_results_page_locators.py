from selenium.webdriver.common.by import By


class EbaySearchResultsPageLocators:
    FILTER_BASE = (By.XPATH, '//li[@class and .//h3[text() = "{}"]]//span[text() = "{}"]')
    SEARCH_RESULTS = (By.XPATH, '//div[@id="srp-river-results"]//li[@id]//span[@role="heading"]/ancestor::a')
    BUY_IT_NOW_FILTER = (By.XPATH, '//ul[@class="fake-tabs__items"]//span[text()="Buy It Now"]')
    AUCTION_FILTER = (By.XPATH, '//ul[@class="fake-tabs__items"]//span[text()="Auction"]')


from selenium.webdriver.common.by import By


class AmazonSearchResultsPageLocators:
    FILTER_SECTION = (By.XPATH, '//div[@id="s-refinements"]//div[@id and ./div/span[contains(text(),"{text}")]]')
    RESULTS = (By.XPATH, '//div[@data-component-type="s-search-result"]//span[@class="a-size-base-plus a-color-base a-text-normal"]')

from selenium.webdriver.common.by import By


class EbayMainPageLocators:
    SEARCH_INPUT = (By.ID, 'gh-ac')
    SEARCH_BUTTON = (By.XPATH, '//input[@type="submit"]')
    SIGN_IN_BUTTON = (By.XPATH, '//span[@id="gh-ug"]/a')
    REGISTER_BUTTON = (By.XPATH, '//span[@id="gh-ug"]/span/a')
    DAILY_DEALS_BUTTON = (By.XPATH, '//li[@id="gh-p-1"]/a')
    BRAND_OUTLET_BUTTON = (By.XPATH, '//li[@id="gh-p-4"]/a')
    HELP_CONTACTS_BUTTON = (By.XPATH, '//li[@id="gh-p-3"]/a')
    SELL_BUTTON = (By.XPATH, '//li[@id="gh-p-2"]/a')
    WATCHLIST_BUTTON = (By.CSS_SELECTOR, 'li[id="gh-wl-click"] a.watchlist-menu')
    MY_EBAY_BUTTON = (By.CSS_SELECTOR, 'li[id="gh-eb-My"] a[class="gh-eb-li-a gh-rvi-menu"]')
    MY_EBAY_LIST = (By.XPATH, '//ul[@id="gh-ul-nav"]/li')
    SHOP_BY_CATEGORY_BUTTON = (By.XPATH, '//button[@id="gh-shop-a"]')
    SAVED_TAB = (By.XPATH, '//li[@class="saved"]')
    TABS_LIST = (By.XPATH, '//li[@data-currenttabindex]')

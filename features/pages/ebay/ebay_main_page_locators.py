from enum import Enum


class EbayMainPageLocators:
    SEARCH_INPUT = {'id': 'gh-ac'}
    SEARCH_BUTTON = {'xpath': '//input[@type="submit"]'}
    SIGN_IN_BUTTON = {'xpath': '//span[@id="gh-ug"]/a'}
    REGISTER_BUTTON = {'xpath': '//span[@id="gh-ug"]/span/a'}
    DAILY_DEALS_BUTTON = {'xpath': '//li[@id="gh-p-1"]/a'}
    BRAND_OUTLET_BUTTON = {'xpath': '//li[@id="gh-p-4"]/a'}
    HELP_CONTACTS_BUTTON = {'xpath': '//li[@id="gh-p-3"]/a'}
    SELL_BUTTON = {'xpath': '//li[@id="gh-p-2"]/a'}
    WATCHLIST_BUTTON = {'css': 'li[id="gh-wl-click"] a.watchlist-menu'}
    MY_EBAY_BUTTON = {'css': 'li[id="gh-eb-My"] a[class="gh-eb-li-a gh-rvi-menu"]'}
    MY_EBAY_LIST = {'xpath': '//ul[@id="gh-ul-nav"]/li'}
    SHOP_BY_CATEGORY_BUTTON = {'xpath': '//button[@id="gh-shop-a"]'}
    SAVED_TAB = {'xpath': '//li[@class="saved"]'}
    TABS_LIST = {'xpath': '//li[@data-currenttabindex]'}

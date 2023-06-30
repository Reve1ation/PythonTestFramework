from features.pages.ebay.generic_ebay_page import GenericEbayPage


class EbayMainPage(GenericEbayPage):

    URL = 'https://www.ebay.com'

    def __init__(self, context):
        super().__init__(context)

    @property
    def search_input(self):
        return self.find_element(id='gh-ac')

    @property
    def search_button(self):
        return self.find_element(xpath='//input[@type="submit"]')

    @property
    def sigh_in_button(self):
        return self.find_element(xpath='//span[@id="gh-ug"]/a')

    @property
    def register_button(self):
        return self.find_element(xpath='//span[@id="gh-ug"]/span/a')

    @property
    def daily_deals_button(self):
        return self.find_element(xpath='//li[@id="gh-p-1"]/a')

    @property
    def brand_outlet_button(self):
        return self.find_element(xpath='//li[@id="gh-p-4"]/a')

    @property
    def help_contacts_button(self):
        return self.find_element(xpath='//li[@id="gh-p-3"]/a')

    @property
    def sell_button(self):
        return self.find_element(xpath='//li[@id="gh-p-2"]/a')

    @property
    def watchlist_button(self):
        return self.find_element(css='li[id="gh-wl-click"] a.watchlist-menu')

    @property
    def my_ebay_button(self):
        return self.find_element(css='li[id="gh-eb-My"] a[class="gh-eb-li-a gh-rvi-menu"]')

    @property
    def my_ebay_list(self):
        return self.find_elements(xpath='//ul[@id="gh-ul-nav"]/li')

    @property
    def shop_by_category_button(self):
        return self.find_element(xpath='//button[@id="gh-shop-a"]')

    @property
    def saved_tab(self):
        return self.find_element(xpath='//li[@class="saved"]')

    @property
    def tabs_list(self):
        return self.find_elements(xpath='//li[@data-currenttabindex]')

    def load(self):
        self.driver.get(self.URL)
        return self

    def navigate_to_tab_by_text(self, text):
        for element in self.tabs_list:
            if element.get_attribute("value") == text:
                return element

    def verify_elements_present(self):
        pass

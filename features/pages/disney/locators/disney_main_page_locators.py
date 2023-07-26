from selenium.webdriver.common.by import By


class DisneyMainPageLocators:
    DISNEY_HEADER_MENUS = (By.XPATH, '//ul[@id="goc-desktop-global"]/li[./div]/a')
    ADVERTISEMENT = (By.XPATH, '//section[@id="overlay" and @class="overlayClose"]')
    THIRD_PARTY_IFRAME = (By.XPATH, '//iframe[@title="3rd party ad content"]')

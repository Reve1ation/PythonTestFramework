from selenium.webdriver.common.by import By


class AddToCartWidgetLocators:
    POP_UP_HEADER = (By.XPATH, '//div[@data-testid="ux-overlay"]//div[@class="app-atc-layer-header-wrapper"]/h2')
    CLOSE_POP_UP_BUTTON = (By.XPATH, '//button[@class="clzBtn viicon-close"]')



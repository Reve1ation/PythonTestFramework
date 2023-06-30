from features.pages.page import Page


class AddToCartWidget(Page):
    ITEM_ADDED_TEXT = "added to cart"

    def __init__(self, context):
        super().__init__(context)
        self.context = context

    @property
    def pop_up_header(self):
        return self.find_element(xpath='//div[@data-testid="ux-overlay"]//div[@class="app-atc-layer-header-wrapper"]/h2')

    @property
    def close_pop_up_button(self):
        return self.find_element(xpath='//button[@class="clzBtn viicon-close"]')

    def close(self):
        self.close_pop_up_button.click()

    def item_is_added(self):
        return self.ITEM_ADDED_TEXT in self.pop_up_header.text

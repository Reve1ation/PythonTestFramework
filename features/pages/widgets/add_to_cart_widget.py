from features.pages.page import Page
from features.pages.widgets.add_to_cart_widget_locators import AddToCartWidgetLocators


class AddToCartWidget(Page):
    ITEM_ADDED_TEXT = "added to cart"

    def __init__(self, context):
        super().__init__(context)
        self.context = context

    def pop_up_header(self):
        return self.find_element(AddToCartWidgetLocators.POP_UP_HEADER)

    def close_pop_up_button(self):
        return self.find_element(AddToCartWidgetLocators.CLOSE_POP_UP_BUTTON)

    def close(self):
        self.close_pop_up_button().click()

    def item_is_added(self):
        return self.ITEM_ADDED_TEXT in self.pop_up_header().text

from behave import given, when, then

from features.pages.ebay.ebay_cart_page import EbayCartPage
from features.pages.ebay.ebay_item_details_page import EbayItemDetailsPage
from features.pages.ebay.ebay_search_results_page import EbaySearchResultsPage


@when('the user enters "{search_text}" in the search bar')
def step_when_user_enters_to_search_bar(context, search_text):
    context.search_results = search_text
    context.page.search_input.clear()
    context.page.search_input.send_keys(search_text)


@when('the user selects the "random" item')
def step_when_the_user_select_random_item(context):
    context.page = EbaySearchResultsPage(context)
    context.page.open_random_item()
    context.page = EbayItemDetailsPage(context)


@then("the eBay search results page is displayed")
def step_then_search_results_displayed(context):
    context.page = EbaySearchResultsPage(context)
    assert context.page.results_contains_text(context.search_results), "One or more results has unexpected text"


@then("the cart page is displayed")
def step_then_search_results_displayed(context):
    context.page = EbayCartPage(context)
    assert context.page.verify_elements_present(), "One or more results has unexpected text"


@then("the item is added to the cart")
def step_item_added_to_cart(context):
    assert context.page.add_to_cart_widget.item_is_added, "Item wasn't added to cart"
    context.page.add_to_cart_widget.close()


@when('user selects the "{value}" filter')
def step_when_user_selects_sell_filter(context, value):
    context.page = EbaySearchResultsPage(context)
    match value:
        case "Auction":
            context.page.sell_type_filter_auction.click()
        case "Buy It Now":
            context.page.sell_type_filter_buy_now.click()
        case _:
            raise Exception(f"{value} is not present in the filter")


@then("the item is removed from the cart")
def step_then_item_was_removed(context):
    cart_page = EbayCartPage(context)
    item_removed = cart_page.verify_item_removed()
    assert item_removed, "The item was not removed from the cart"


@when("the user removes one random item from the cart")
def step_when_user_removes_cart_item(context):
    context.page.remove_random_item()
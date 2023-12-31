from behave import given, when, then

from features.pages.ebay.ebay_search_results_page import EbaySearchResultsPage
from features.pages.google.google_search_page import GoogleSearchPage
from features.pages.ebay.ebay_main_page import EbayMainPage
from features.pages.ebay.ebay_cart_page import EbayCartPage


@given('the user opens {page_name}')
def step_given_user_on_generic_page(context, page_name):
    class_name = ''.join(word.capitalize() for word in page_name.split())
    context.page = eval(class_name)(context)
    context.page.load()


@when('the user clicks the "{button_name}" button 1111')
def the_user_clicks_button(context, button_name):
    button = '_'.join(button_name.lower().split())
    button_element = getattr(context.page, f"{button}_button")
    if button_element():
        button_element().click()
    else:
        raise ValueError(f"The '{button_name}' button was not found on the page")

    match button_name.lower():
        case "add to cart":
            context.line_items_count = getattr(context, "line_items_count", 0) + 1
        case "remove":
            context.line_items_count -= 1


@then("the {page_name} is displayed")
def step_then_search_results_displayed(context, page_name):
    class_name = ''.join(word.capitalize() for word in page_name.split())
    context.page = eval(class_name)(context)
    assert context.page.verify_elements_present(), "One or more results has unexpected text"

from behave import given, when, then

from features.pages.disney.disney_main_page import DisneyMainPage
from features.pages.amazon.amazon_main_page import AmazonMainPage
from features.pages.amazon.amazon_search_results_page import AmazonSearchResultsPage
from features.pages.ebay.ebay_search_results_page import EbaySearchResultsPage
from features.pages.google.google_search_page import GoogleSearchPage
from features.pages.ebay.ebay_main_page import EbayMainPage
from features.pages.ebay.ebay_cart_page import EbayCartPage


@given('the user opens {page_name}')
def step_given_user_on_generic_page(context, page_name):
    class_name = ''.join(word.capitalize() for word in page_name.split())
    context.page = eval(class_name)(context)
    context.page.load()


@then("the {page_name} is displayed")
def step_then_search_results_displayed(context, page_name):
    class_name = ''.join(word.capitalize() for word in page_name.split())
    context.page = eval(class_name)(context)
    assert context.page.verify_elements_present(), "One or more results has unexpected text"

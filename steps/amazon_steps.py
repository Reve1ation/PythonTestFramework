from behave import given, when, then

from features.pages.amazon.amazon_search_results_page import AmazonSearchResultsPage
from features.pages.ebay.ebay_cart_page import EbayCartPage
from features.pages.ebay.ebay_item_details_page import EbayItemDetailsPage
from features.pages.ebay.ebay_main_page import EbayMainPage
from features.pages.ebay.ebay_search_results_page import EbaySearchResultsPage
from features.pages.ebay.ebay_signin_page import EbaySingInPage


@when('search "" in the search field"')
def step_when_search_text_in_field(context, text):
    context.page.search_for_item(text)
    context.page = AmazonSearchResultsPage(context)


@when('search "{text}" in the search field')
def step_impl(context, text):
    context.page.search_for_item(text)
    context.page = AmazonSearchResultsPage(context)


@when('the user in "{filter_section}" filter selects "{filter_option}"')
def step_user_select_filter_option(context, filter_section, filter_option):
    context.page.select_side_filter_option(filter_section, filter_option)


@then('user verify all results have "{expected_text}" text in it')
def step_user_verify_results_text(context, expected_text):
    assert context.page.verify_item_text(expected_text)

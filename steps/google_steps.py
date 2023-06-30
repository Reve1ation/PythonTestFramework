from behave import then


# @given('the user is on the Google search page')
# def step_given_user_on_google_search_page(context):
#     context.page = GoogleSearchPage(context)
#     context.page.load()


@then('the search field is present')
def step_then_search_field_present(context):
    assert context.page.search_input, "Search field is not present"

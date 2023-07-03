from behave import given, when, then


@then('the search field is present')
def step_then_search_field_present(context):
    assert context.page.search_input, "Search field is not present"

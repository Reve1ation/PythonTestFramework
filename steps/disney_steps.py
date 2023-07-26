from behave import given, when, then

from features.pages.disney.disney_second_page import DisneySecondPage


@when("the user navigate to {main_menu}")
def step_when_user_click_header_menu(context, main_menu):
    context.page.open_header_menu_page(main_menu)
    context.page = DisneySecondPage(context)


@when("the user hover {main_menu} and select {sub_menu}")
def step_when_user_click_header_menu(context, main_menu, sub_menu):
    context.page.open_sub_menu_page(main_menu, sub_menu)
    context.page = DisneySecondPage(context)


@then('Check that page has {title}')
def check_title_page(context, title):
    actual_title = context.driver.title
    assert title == actual_title, f"Title is wrong! Expected title:{title}, Actual result:{actual_title}"

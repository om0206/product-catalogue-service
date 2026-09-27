"""Reusable web step definitions for Product Catalogue BDD tests."""
from behave import then, when


@when('I press the "{button}" button')
def step_press_button(context, button):
    context.browser.find_element("xpath", f"//button[normalize-space()='{button}']").click()


@then('I should see "{text}"')
def step_see_text(context, text):
    assert text in context.browser.page_source


@then('I should not see "{text}"')
def step_not_see_text(context, text):
    assert text not in context.browser.page_source


@then('I should see a message "{message}"')
def step_see_message(context, message):
    assert message in context.browser.page_source

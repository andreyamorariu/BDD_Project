from behave import *

@when('forgot_password: I set my email "{email}"')
def step_impl(context, email):
    context.forgot_pass_page.set_email(email)

@then('forgot_password: I verify that email validation message is correct')
def step_impl(context):
    context.forgot_pass_page.verify_email_error_msg()
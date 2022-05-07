from behave import *

# given!, when!, and, but, then! - sintaxa gherkin
# given - seteaza situatia initiala
# when - pasii din test
# then - verificarea din test

@given('signin: I am a user on Jules signin page')
def step_impl(context):
    context.signin_page.navigate_to_login_page()

@when('signin: I set my email "{email}"')
def step_impl(context, email):
    context.signin_page.set_email()

@when('signin: I set my password "{password}"')
def step_impl(context, password):
    context.signin_page.set_pass()

@when('signin: I click on login button')
def step_impl(context):
    context.signin_page.click_login()

@when('signin: I click on forgot_password_link')
def step_impl(context):
    context.signin_page.click_forgot_password_link()
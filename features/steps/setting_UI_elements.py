from behave import given, when, then
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given('Open the main page')
def open_main_page(context):
    context.app.log_in_page.open_log_in_page()


@when('Log in to the page, email: {email} password: {password}')
def log_in(context, email, password):
    context.app.log_in_page.login_user(email, password)
    sleep(5)


@then('Click on settings option')
def click_setting(context):
    setting_button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable(context.app.setting_page.SETTING_BUTTON)
    )
    setting_button.click()


@then('Verify the right page opens')
def setting_page_url(context):
    context.app.setting_page.setting_page_url()


@then('Verify there are {amount} options for the settings')
def settings_options(context, amount):
    amount = int(amount)
    context.app.setting_page.setting_options(amount)


@then('Verify “connect the company” button is available')
def connect_company_button(context):
    context.app.setting_page.connect_company_button()

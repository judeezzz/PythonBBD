from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given(u'I launch chrome browser')
def launchBrowser(context):
    context.driver = webdriver.Chrome()


@when(u'I open sauce demo homepage')
def step_impl(context):
    context.driver.get("https://www.saucedemo.com/")


@when(u'enter username "{user}" and password "{pwd}"')
def step_impl(context, user, pwd):
    context.driver.find_element(By.ID, 'user-name').send_keys(user)
    context.driver.find_element(By.ID, 'password').send_keys(pwd)


@when(u'click login button')
def step_impl(context):
    context.driver.find_element(By.ID, 'login-button').click()


@then(u'user must successfully login to Dashboard page')
def step_impl(context):
    try:
        status = context.driver.find_element(By.ID, 'inventory_container').is_displayed()
    except:
        context.driver.close()
        assert False, "Test Failed"

    if status is True:
        assert True, "Test Passed"
        context.driver.close()

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given(u'launch chrome browser')
def launchBrowser(context):
    context.driver = webdriver.Chrome()


@when(u'open saucedemo website')
def openHomePage(context):
    context.driver.get("https://www.saucedemo.com/")


@then(u'verify logo present on the page')
def verifyLog(context):
    status = context.driver.find_element(By.CLASS_NAME, "login_logo").is_displayed()
    assert status is True


@then(u'close browser')
def closeBrowser(context):
    context.driver.close()

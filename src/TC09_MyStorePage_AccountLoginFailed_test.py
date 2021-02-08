import os
import sys; sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from selenium import webdriver
from pages.mystore_page import MyStorePage
import json

# # # Test setup
with open('element_locator.json', 'r') as ms:
    data = json.load(ms)
sign_in_button = data["sign_in_button"]
login_email_input_field = data["login_email_input"]
login_password_input_field = data["login_password_input"]
submit_login_button = data["submit_login_button"]
authentication_error = data["account_error"]


browser = webdriver.Chrome()
browser.maximize_window()

my_account_url = 'http://automationpractice.com/index.php?controller=my-account'
'''
set valid inputs:
Before test execution have to set up email and/or password to be incorrect
'''
# email_address = "vladimir.kocis.tubic@gmail.com"  # correct email
email_address = "vlada.kocis.tubic@gmail.com"  # incorrect email

acc_password = "testPass1"  # correct password
# acc_password = "testPass1_z"  # incorrect password

error_message = 'There is 1 error'

my_store = MyStorePage(browser)
my_store.go()


# # # TEST
def test_account_login_failed():
    """
    Test Case created to check if entering incorrect email or/and incorrect password
    and clicking on sign in button leads to alert message.
    Test passes if alert message appears
    """
    # find and click on sign in button
    sign_in_btn = my_store.element(sign_in_button)
    sign_in_btn.find()
    sign_in_btn.click()

    # find and populate login email input field
    login_email_input = my_store.element(login_email_input_field)
    login_email_input.find()
    login_email_input.populate_field(email_address)

    # find and populate login password input field
    login_password_input = my_store.element(login_password_input_field)
    login_password_input.find()
    login_password_input.populate_field(acc_password)

    # find and click on sign in button
    submit_login_btn = my_store.element(submit_login_button)
    submit_login_btn.find()
    submit_login_btn.click()

    # find account creation error pop up
    authentic_error = my_store.element(authentication_error)
    authentic_error.find()
    authentic_error_msg = authentic_error.text()

    # compare alert messages if appear
    assert authentic_error_msg == error_message

    # close Google Chrome browser
    browser.close()





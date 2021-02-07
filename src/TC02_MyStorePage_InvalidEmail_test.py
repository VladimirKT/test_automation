import os
import sys; sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from selenium import webdriver
from pages.mystore_page import MyStorePage
import json

# Test setup
with open('element_locator.json', 'r') as ms:
    data = json.load(ms)
sign_in_button = data["sign_in_button"]
email_input_field = data["email_input_field"]
create_account_button = data["create_account_button"]
account_error_li = data["account_error_li"]
browser = webdriver.Chrome()
browser.maximize_window()

my_store = MyStorePage(browser)
my_store.go()

invalid_email = "vladimir@vladimir"


def test_invalid_email():
    # find and click on sign in button
    sign_in_btn = my_store.element(sign_in_button)
    sign_in_btn.find()
    sign_in_btn.click()

    # find and populate email input field
    email_input = my_store.element(email_input_field)
    email_input.find()
    email_input.populate_field(invalid_email)

    # find and click on create account button
    create_acc_btn = my_store.element(create_account_button)
    create_acc_btn.find()
    create_acc_btn.click()

    # find and compare error message
    account_error = my_store.element(account_error_li)
    account_error.find()
    assert account_error.text() == "Invalid email address."

    # close Google Chrome browser
    browser.close()

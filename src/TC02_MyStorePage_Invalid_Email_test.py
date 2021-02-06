import os
import sys; sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from selenium import webdriver
from pages.mystore_page import MyStorePage
import json

# Test setup
with open('mystore_locators.json', 'r') as ms:
    data = json.load(ms)
sign_in_btn = data["sign_in_btn"]
email_input = data["email_input_field"]
create_acc_btn = data["create_account_btn"]
account_error = data["account_error"]
browser = webdriver.Chrome()
browser.maximize_window()

my_store = MyStorePage(browser)
my_store.go()

invalid_input = "vladimir@vladimir"


def test_invalid_email():
    my_store.element(sign_in_btn).click()
    my_store.element(email_input).enter_text(invalid_input)
    my_store.element(create_acc_btn).click()
    error_text = my_store.element(account_error).text()
    assert error_text == "Invalid email address."
    browser.close()
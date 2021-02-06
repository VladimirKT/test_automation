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
browser = webdriver.Chrome()
browser.maximize_window()

my_store = MyStorePage(browser)
my_store.go()

valid_input = "vladimir@vladimir.com"

valid_acc_url = "http://automationpractice.com/index.php?controller=authentication&back=my-account#account-creation"


def test_valid_email():
    my_store.element(sign_in_btn).click()
    my_store.element(email_input).enter_text(valid_input)
    my_store.element(create_acc_btn).click()
    current_url = browser.current_url
    print(current_url)
    # assert current_url == valid_acc_url
    # browser.close()
    

test_valid_email()
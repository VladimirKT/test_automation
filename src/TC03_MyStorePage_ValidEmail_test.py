import os
import sys; sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from selenium import webdriver
from pages.mystore_page import MyStorePage
import json

# # # Test setup
with open('element_locator.json', 'r') as ms:
    data = json.load(ms)
sign_in_button = data["sign_in_button"]
email_input_field = data["email_input_field"]
create_account_button = data["create_account_button"]
browser = webdriver.Chrome()
browser.maximize_window()

my_store = MyStorePage(browser)
my_store.go()

valid_email = "vladimir@test.rs"

create_acc_url = "http://automationpractice.com/index.php?controller=authentication&back=my-account#account-creation"


# # # TEST
def test_valid_email():
    """
    Test Case created to check if entering correct email form
    and clicking on create account button leads to create account page.
    Test passes if page url is correct
    """
    # find and click on sign in button
    sign_in_btn = my_store.element(sign_in_button)
    sign_in_btn.find()
    sign_in_btn.click()

    # find and populate email input field
    email_input = my_store.element(email_input_field)
    email_input.find()
    email_input.populate_field(valid_email)

    # find and click on create account button
    create_acc_btn = my_store.element(create_account_button)
    create_acc_btn.find()
    create_acc_btn.click()

    # compare current url with url after click on create account button
    create_acc_btn.url_to_be(create_acc_url)
    current_url = browser.current_url
    assert current_url == create_acc_url

    # close Google Chrome browser
    browser.close()
    


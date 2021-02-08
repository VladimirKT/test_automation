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


browser = webdriver.Chrome()
browser.maximize_window()

my_account_url = 'http://automationpractice.com/index.php?controller=my-account'

email_address = "vladimir.kocis.tubic@gmail.com"
acc_password = "testPass1"

my_store = MyStorePage(browser)
my_store.go()


# # # TEST
def test_account_login():
    """
    Test Case created to check if entering correct email and password
    and clicking on submit login button leads to my account page.
    Test passes if page url is correct
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

    # compare current url with url after click on submit account button
    submit_login_btn.url_to_be(my_account_url)
    current_url = browser.current_url
    assert current_url == my_account_url

    # close Google Chrome browser
    browser.close()


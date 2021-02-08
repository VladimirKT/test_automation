import os
import sys; sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from selenium import webdriver
from pages.mystore_page import MyStorePage
import json

# # # Test setup
with open('element_locator.json', 'r') as ms:
    data = json.load(ms)
sign_in_button = data["sign_in_button"]
forgot_password_link = data["forgot_password_link"]
forgot_pass_email_input_field = data["forgot_pass_email_input"]
retrieve_password_button = data["retrieve_password_button"]
reset_password_alert = data["reset_password_alert"]

browser = webdriver.Chrome()
browser.maximize_window()

my_account_url = 'http://automationpractice.com/index.php?controller=my-account'

email_address = "vladimir.kocis.tubic@gmail.com"

confirmation_email_msg = f"A confirmation email has been sent to your address: {email_address}"

my_store = MyStorePage(browser)
my_store.go()


# # # TEST
def test_reset_password():
    """
    Test Case created to check if entering correct email
    and clicking on retrieve password button leads to confirmation message.
    Test passes if confirmation message "A confirmation email has been sent to your address" appears
    """
    # find and click on sign in button
    sign_in_btn = my_store.element(sign_in_button)
    sign_in_btn.find()
    sign_in_btn.click()

    # find and click on forgot password link
    forgot_pass_link = my_store.element(forgot_password_link)
    forgot_pass_link.find()
    forgot_pass_link.click()

    # find and populate login email input field
    forgot_pass_email_input = my_store.element(forgot_pass_email_input_field)
    forgot_pass_email_input.find()
    forgot_pass_email_input.populate_field(email_address)

    # find and click on retrieve password button
    retrieve_pass_btn = my_store.element(retrieve_password_button)
    retrieve_pass_btn.find()
    retrieve_pass_btn.click()

    # find confirmation password alert message and compare with hard coded password email msg
    reset_pass_alert = my_store.element(reset_password_alert)
    reset_pass_alert.find()
    reset_password_msg = reset_pass_alert.text()
    assert reset_password_msg == confirmation_email_msg

    # close Google Chrome browser
    browser.close()


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
mr_gender_label = data["mr_gender"]
first_name_input = data["first_name_input"]
last_name_input = data["last_name_input"]
passwd_input_field = data["passwd_input"]
address1_input_field = data["address1_input"]
city_input_field = data["city_input"]
state_select_tag = data["state_select_tag"]
state_select_option = data["state_select_option"]
post_code_input_field = data["post_code_input"]
country_select_tag = data["country_select_tag"]
country_select_option = data["country_select_option"]
mobile_phone_input_field = data["mobile_phone_input"]
submit_account_button = data["submit_account_button"]

browser = webdriver.Chrome()
browser.maximize_window()

my_store = MyStorePage(browser)
my_store.go()

'''
set valid inputs:
Change valid_email for every single test run. After account is created with one email address,
second test run must be with different email. Otherwise, test is going to fail.
That is not real error (false positive)
Other inputs (valid_inputs) can stay as is..
'''

# valid_email = "vladimir.kocis.tubic@gmail.com"
valid_email = "vladimirkt@gmail.com"

valid_inputs = ['Vladimir', 'Kocis Tubic', "testPass1", "Palmira Toljatija 54", "Belgrade", '3', '11000', "21", "0641754469"]

my_account_url = "http://automationpractice.com/index.php?controller=my-account"


def test_create_account():

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

    # find and click on mr gender field
    mr_gender = my_store.element(mr_gender_label)
    mr_gender.find()
    mr_gender.click()

    # find and populate first name input field
    first_name = my_store.element(first_name_input)
    first_name.find()
    first_name.populate_field(valid_inputs[0])

    # find and populate last name input field
    last_name = my_store.element(last_name_input)
    last_name.find()
    last_name.populate_field(valid_inputs[1])

    # find and populate password input field
    passwd_input = my_store.element(passwd_input_field)
    passwd_input.find()
    passwd_input.populate_field(valid_inputs[2])

    # find and populate address1 input field
    address1_input = my_store.element(address1_input_field)
    address1_input.find()
    address1_input.populate_field(valid_inputs[3])

    # find and populate city input field
    city_input = my_store.element(city_input_field)
    city_input.find()
    city_input.populate_field(valid_inputs[4])

    # find and click on state selected option field
    state_select = my_store.element(state_select_tag)
    state_select.find()
    state_select.click()
    state_option = my_store.element(state_select_option)
    state_option.find_select_tag(valid_inputs[5])

    # find and populate post code input field
    post_code_input = my_store.element(post_code_input_field)
    post_code_input.find()
    post_code_input.populate_field(valid_inputs[6])

    # find and click on country selected option field
    country_select = my_store.element(country_select_tag)
    country_select.find()
    country_select.click()
    country_option = my_store.element(country_select_option)
    country_option.find_select_tag(valid_inputs[7])

    # find and populate mobile phone input field
    mobile_phone_input = my_store.element(mobile_phone_input_field)
    mobile_phone_input.find()
    mobile_phone_input.populate_field(valid_inputs[8])

    # find and click on submit account button
    submit_acc_btn = my_store.element(submit_account_button)
    submit_acc_btn.find()
    submit_acc_btn.click()

    # compare current url with url after click on submit account button
    submit_acc_btn.url_to_be(my_account_url)
    current_url = browser.current_url
    assert current_url == my_account_url

    # close Google Chrome browser
    browser.close()



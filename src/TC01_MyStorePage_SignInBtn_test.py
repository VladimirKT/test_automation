import os
import sys; sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from selenium import webdriver
from pages.mystore_page import MyStorePage
import json

# Test setup
with open('element_locator.json', 'r') as ms:
    data = json.load(ms)
sign_in_button = data["sign_in_button"]
browser = webdriver.Chrome()
browser.maximize_window()

sign_in_url = 'http://automationpractice.com/index.php?controller=authentication&back=my-account'

my_store = MyStorePage(browser)
my_store.go()


def test_sign_in_btn():
    # find and click on sign in button
    sign_in_btn = my_store.element(sign_in_button)
    sign_in_btn.find()
    sign_in_btn.click()

    # compare current url with url after click on sign in button
    current_url = browser.current_url
    assert current_url == sign_in_url

    # close Google Chrome browser
    browser.close()

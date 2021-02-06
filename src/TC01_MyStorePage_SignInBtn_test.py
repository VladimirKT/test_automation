import os
import sys; sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from selenium import webdriver
from pages.mystore_page import MyStorePage
import json

# Test setup
with open('mystore_locators.json', 'r') as ms:
    data = json.load(ms)
sign_in_btn = data["sign_in_btn"]
browser = webdriver.Chrome()
browser.maximize_window()

sign_in_url = 'http://automationpractice.com/index.php?controller=authentication&back=my-account'

my_store = MyStorePage(browser)
my_store.go()


def test_sign_in_btn():
    my_store.element(sign_in_btn).click()
    current_url = browser.current_url
    assert current_url == sign_in_url
    browser.close()

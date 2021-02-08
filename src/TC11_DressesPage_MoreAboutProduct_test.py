import os
import sys; sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from selenium import webdriver
from pages.dresses_page import DressesPage
import json

# # # Test setup
with open('element_locator.json', 'r') as ms:
    data = json.load(ms)
product = data["product4"]
more_button = data["more_btn_prod4"]

product_url = 'http://automationpractice.com/index.php?id_product=4&controller=product'

browser = webdriver.Chrome()
browser.maximize_window()
dresses_page = DressesPage(browser)
dresses_page.go()


# # # TEST
def test_more_about_product():
    """
    Test Case created to check if hovering over product
    and clicking on more button leads to more about product page.
    Test passes if page url is correct
    """
    # find and hover over product
    dress_product = dresses_page.element(product)
    dress_product.find()
    dress_product.hover()

    # find and click on more button
    more_btn = dresses_page.element(more_button)
    more_btn.find()
    more_btn.click()

    # compare current url with url after click on more button
    current_url = browser.current_url
    assert current_url == product_url

    # close Google Chrome browser
    browser.close()

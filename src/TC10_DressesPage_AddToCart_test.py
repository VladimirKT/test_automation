import os
import sys; sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from selenium import webdriver
from pages.dresses_page import DressesPage
import json

# # # Test setup
with open('element_locator.json', 'r') as ms:
    data = json.load(ms)
product = data["product3"]
add_button = data["add_btn_prod3"]
add_to_cart = data["add_to_cart"]

success_added_msg = "Product successfully added to your shopping cart"

browser = webdriver.Chrome()
browser.maximize_window()
dresses_page = DressesPage(browser)
dresses_page.go()


# # # TEST
def test_add_to_cart():
    """
    Test Case created to check if hovering over product
    and clicking on add to cart button leads to add to cart page.
    Test passes if page url is correct
    """
    # find and hover over product
    dress_product = dresses_page.element(product)
    dress_product.find()
    dress_product.hover()

    # find and click on add to cart button
    add_btn = dresses_page.element(add_button)
    add_btn.find()
    add_btn.click()

    # find add to cart page and check message
    add_to_cart_page = dresses_page.element(add_to_cart)
    add_to_cart_page.find()
    add_to_cart_msg = add_to_cart_page.text()
    assert add_to_cart_msg == success_added_msg

    # close Google Chrome browser
    browser.close()

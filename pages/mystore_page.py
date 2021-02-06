import os
import sys; sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from selenium.webdriver.common.by import By
from lib.base_page import BasePage
from lib.base_element import BaseElement


class MyStorePage(BasePage):

    url = "http://automationpractice.com/index.php"

    def __init__(self, driver):
        self.driver = driver

    def element(self, loc):
        locator = (By.XPATH, loc)
        return BaseElement(driver=self.driver, locator=locator)



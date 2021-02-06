from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains as AC


class BaseElement:

    def __init__(self, driver, locator):
        self.driver = driver
        self.locator = locator
        self.web_element = None
        self.find()

    def __len__(self):
        return len(self.web_element)

    def find(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.locator))
        self.web_element = element

    def click(self):
        EC.element_to_be_clickable(self.locator)
        self.web_element.click()

    def text(self):
        text = self.web_element.text
        return text

    def enter_text(self, int_text):
        self.web_element.send_keys(int_text)

    def hover(self):
        AC(self.driver).move_to_element(self.web_element).perform()

    def get_attribute_value(self, attr):
        attribute_value = self.web_element.get_attribute(attr)
        return attribute_value

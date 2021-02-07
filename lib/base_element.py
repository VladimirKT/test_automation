from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains as AC
from selenium.webdriver.support.select import Select


class BaseElement:

    def __init__(self, driver, locator):
        self.driver = driver
        self.locator = locator
        self.web_element = None
        self.web_elements = None
        # self.find()

    def __len__(self):
        return len(self.web_element)

    def find(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.locator))
        self.web_element = element

    def find_select_tag(self, value_st):
        select_option = Select(self.driver.find_element_by_xpath(self.locator[1]))
        select_option.select_by_value(value_st)

    def click(self):
        EC.element_to_be_clickable(self.locator)
        self.web_element.click()

    def text(self):
        text = self.web_element.text
        return text

    def populate_field(self, int_text):
        self.web_element.send_keys(int_text)

    def hover(self):
        AC(self.driver).move_to_element(self.web_element).perform()

    def get_attribute_value(self, attr):
        attribute_value = self.web_element.get_attribute(attr)
        return attribute_value

    def url_to_be(self, url):
        valid_url = WebDriverWait(self.driver, 10).until(
            EC.url_to_be(url))
        return valid_url




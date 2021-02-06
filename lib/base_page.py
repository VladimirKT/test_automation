class BasePage:

    def go(self):
        self.driver.get(self.url)

from selenium import webdriver
class RandomElement:
    def __init__(self, driver, locator):
        self.locator = locator
        self.element = driver.find_element(self.locator[0], self.locator[1])





    # def find_element(self):
        



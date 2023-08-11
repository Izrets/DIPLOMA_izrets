import random
from selenium import webdriver
from selenium.webdriver import Keys
from Automation.mainlogic.locators import Locators
from selenium.webdriver.common.by import By
from Automation.mainlogic._init_ import Business
from Automation.browser_chrome import Browser
import logging
from random import randint

LOGGER = logging.getLogger(__name__)

class Element:
    def __init__(self, driver, locator):
        self.driver = driver
        self.locator = locator
        self.element = driver.find_element(self.locator[0], self.locator[1])
        # shadow_div = driver.find_element(By.ID, "frontegg-login-box-container-default")
        # self.element = shadow_div.shadow_root.find_element(self.locator[0], self.locator[1])


    def click_element(self):
        self.element.click()

class InputElement(Element):
    def enter_text(self, text):
        LOGGER.debug(f"Получен и введен в поле текст: '{text}'")
        self.click_element()
        self.element.send_keys(text)
    def key_code(self):
        return self.element.send_keys(Keys.ENTER)

    def get_text(self):
        return self.element.get_attribute('value')
class ButtonElement(Element):
    def key_code(self):
        return self.element.click()

# class FindElement(Element):
#     def element_code(self):
#         return self.element

# class random_items_in_stock:
#     def index_of_item_divs(self):
#         self

class Randomdata:
    def __init__(self, count_of_divs, in_stock_items, path_of_button, pseudorandom_locator):
        self.count_of_divs = count_of_divs
        self.in_stock_items = in_stock_items
        self.path_of_button = path_of_button
        self.pseudorandom_locator = pseudorandom_locator

class Random(): #выдаёт номера элементов в наличии из которых будет выбираться случайный для теста
    path = '/books'
    def __init__(self, Browser):
        self.grid = InputElement(driver=Browser.get_driver(), locator=Locators.path_of_grid)
    def get_count_of_divs(self, Browser):
        self.count_of_divs = len(self.grid.find_elements(By.XPATH, "./div"))
        return self.count_of_divs
    def get_in_stock_items(self):
        self.in_stock_items = []
        for i in range(self.count_of_divs):
            path_of_item = (f'/html/body/div[4]/div[1]/div[4]/div[2]/div[2]/div[2]/div[3]/div[{i}]')
            try:
                self.grid.find_element(By.XPATH, path_of_item+self.path_of_button).\
                    get_attribute('value') != 'Add to cart'
            except:
                self.in_stock_items.append(i)
        return self.in_stock_items
    
    def get_random_locator_of_actual_item(self):
        self.path_of_button = Locators.path_of_button
        self.pseudorandom_locator = (By.XPATH, f'/html/body/div[4]/div[1]/div[4]/div[2]/div[2]/div[2]/div[3]/div' \
                                          f'{self.in_stock_items[random.randint(0, self.count_of_divs)]}' \
                                          f'+{self.path_of_button}')
        return self.pseudorandom_locator
        
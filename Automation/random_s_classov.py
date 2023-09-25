from selenium import webdriver
import random
from Automation.mainlogic.element import *

class Random():

    def __init__(self):
        driver = webdriver.Chrome()
        driver.get('https://demowebshop.tricentis.com/books')
        self.grid = driver.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[4]/div[2]/div[2]/div[2]/div[3]')
    def get_path(self):
        # grid = driver.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[4]/div[2]/div[2]/div[2]/div[3]')

        count_of_divs = len(self.grid.find_elements(By.XPATH, "./div"))


        in_stock_items =[]
        for i in range(count_of_divs):
            path_of_item = (f'/html/body/div[4]/div[1]/div[4]/div[2]/div[2]/div[2]/div[3]/div[{i}]')
            #'/html/body/div[4]/div[1]/div[4]/div[2]/div[2]/div[2]/div[3]/div[1]'
            try:
                self.grid.find_element(By.XPATH, path_of_item + Locators.path_of_button).get_attribute('value') != 'Add to cart'
            except:
                in_stock_items.append(i+1)
        print(in_stock_items)


        path_of_button = Locators.path_of_button
        pseudorandom_locator = (f'/html/body/div[4]/div[1]/div[4]/div[2]/div[2]/div[2]/div[3]/div['
                                f'{in_stock_items[random.randint(0, len(in_stock_items)-1)]}'
                                f']{path_of_button}')


        return pseudorandom_locator

r1 = Random()
r1 = r1.get_path()
print(r1)


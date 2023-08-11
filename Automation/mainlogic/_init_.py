
from selenium import webdriver
from selenium.webdriver.common.by import By
from Automation.mainlogic.element import *
from Automation.mainlogic.locators import Locators
# from Automation.browser_chrome import
import logging

import time

LOGGER = logging.getLogger(__name__)


class User:
    def __init__(self, email, password):
        self.email = email
        self.password = password
class SignIn():
    path = '/login'
    def __init__(self, Browser):
        self.email = InputElement(driver=Browser.get_driver(), locator=Locators.email_locator)
        self.password = InputElement(driver=Browser.get_driver(), locator=Locators.password_locator)
        self.login_button = ButtonElement(driver=Browser.get_driver(), locator=Locators.login_button_locator)


    def signin(self, user: User): #логика залогинивания
        LOGGER.info('Start logging in')
        self.email.enter_text(user.email)
        self.password.enter_text(user.password)
        self.login_button.click_element()
        LOGGER.info("Logging in has just been finished")


# class Logic_data: #ex User
#     def __init__(self):
        # cart, checkout, continuee,
        # ground_shipping, continue_shipping, cash, continue_cash,
        #continue_cod, confirm, path_of_list, button_addtocart):
        # self.button_addtocart= button_addtocart
        # self.path_of_list = path_of_list
        # self.confirm = confirm
        # self.continue_cod = continue_cod
        # self.continue_cash = continue_cash
        # self.cash = cash
        # self.continue_shipping = continue_shipping
        # self.ground_shipping = ground_shipping
        # self.continuee = continuee
        # self.checkout = checkout
        # # self.term_of_service = term_of_service
        # self.cart = cart




class Business(): #ex SignUp
    path = '/books'
    def __init__(self, Browser):
        # Randomdata.grid = InputElement(driver=Browser.get_driver(), locator=Locators.path_of_grid)
        self.cart = ButtonElement(driver=Browser.get_driver(), locator=Locators.cart_locator)

        # self.term_of_service = InputElement(driver=Browser.get_driver(), locator=Locators.term_of_service_locator)

        # some pathsss

    def logic_run(self): #шаги проверки бизнес логики ex signup
        LOGGER.info('Start buying')
        R = Random(Browser)
        R = R.get_count_of_divs()
        R = R.get_in_stock_items()
        R = R.get_random_locator_of_actual_item()
        print(R)
        self.addtocart = ButtonElement(driver=Browser.get_driver(),
                                       locator=R)
        self.addtocart.click_element()

        time.sleep(10)
        # print(logicdata.path_of_list+f'/div{randomdata.in_stock_items}'
        #                          f'{[random.randint(0, len(randomdata.in_stock_items))]}'+
        #  logicdata.button_addtocart_location)


        # self.cart.click_element()
        # time.sleep(10)
        # self.InputElement(driver=Browser.get_driver(), locator=Locators.term_of_service_locator).click_element()
        # time.sleep(10)
        # self.InputElement(driver=Browser.get_driver(), locator=Locators.continuee_locator).click_element()
        # self.continue_shipping.click_element()
        # self.cash.click_element()
        # self.continue_cod.click_element()
        # self.confirm.click_element()
        # LOGGER.info("Buying has just been finished")


#         self.continuee = InputElement(driver=Browser.get_driver(), locator=Locators.continuee_locator)
#         self.ground_shipping = InputElement(driver=Browser.get_driver(), locator=Locators.ground_shipping_locator)
#         self.continue_shipping = InputElement(driver=Browser.get_driver(), locator=Locators.continue_shipping_locator)
#         self.cash = InputElement(driver=Browser.get_driver(), locator=Locators.cash_locator)
#         self.continue_cash = ButtonElement(driver=Browser.get_driver(), locator=Locators. continue_cash_locator)
#         self.continue_cod = ButtonElement(driver=Browser.get_driver(), locator=Locators.continue_cod_locator)
#         self.confirm = ButtonElement(driver=Browser.get_driver(), locator=Locators.confirm_locator)
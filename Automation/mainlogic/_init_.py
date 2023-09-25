
from Automation.mainlogic.getxpathofitem import *
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
        self.email.enter_text(user.email)
        self.password.enter_text(user.password)
        self.login_button.click_element()



class LogicRun(): #ex SignUp
    path = '/books'
    def __init__(self, Browser):
        r1 = Random()
        r1 = r1.get_path()
        self.addtocart_btn = InputElement(Browser.get_driver(), r1)
        self.cart = InputElement(Browser.get_driver(), Locators.cart_locator)

    def logicrun(self, Browser): #шаги проверки бизнес логики ex signup
        time.sleep(2)
        self.addtocart_btn.click_element()
        self.cart.click_element()
        InputElement(Browser.get_driver(), Locators.term_of_service_locator).click_element()
        InputElement(Browser.get_driver(), Locators.checkout_locator).click_element()
        InputElement(Browser.get_driver(), Locators.continuee_locator).click_element()
        InputElement(Browser.get_driver(), Locators.in_store_locator).click_element()
        InputElement(Browser.get_driver(), Locators.continuee_in_store_locator).click_element()
        InputElement(Browser.get_driver(), Locators.COD_locator).click_element()
        InputElement(Browser.get_driver(), Locators.continue_cod_locator).click_element()
        InputElement(Browser.get_driver(), Locators.payment_info_continue_locator).click_element()
        InputElement(Browser.get_driver(), Locators.confirm_locator).click_element()
        LOGGER.info('BOUGHT')


        time.sleep(10)




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

        # self.term_of_service = InputElement(driver=Browser.get_driver(), locator=Locators.term_of_service_locator)




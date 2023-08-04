from selenium import webdriver
from selenium.webdriver.common.by import By
from Automation.register.element import Element, InputElement, ButtonElement
from Automation.login.locators import Locators
from Automation.browser_chrome import Browser
import logging

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


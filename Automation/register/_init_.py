from selenium import webdriver
from selenium.webdriver.common.by import By
from Automation.register.element import Element, InputElement, ButtonElement
from Automation.register.locators import Locators
from Automation.browser_chrome import Browser
import logging

LOGGER = logging.getLogger(__name__)

class User:
    def __init__(self, gender, email, first_name, last_name, password, confirm_password):
        self.gender = gender
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.confirm_password = confirm_password




class SignUp():
    path = '/register'
    def __init__(self, Browser):
        self.gender = InputElement(driver=Browser.get_driver(), locator=Locators.user_gender_m_locator)
        self.first_name = InputElement(driver=Browser.get_driver(), locator=Locators.first_name_locator)
        self.last_name = InputElement(driver=Browser.get_driver(), locator=Locators.last_name_locator)
        self.email = InputElement(driver=Browser.get_driver(), locator=Locators.email_locator)
        self.password = InputElement(driver=Browser.get_driver(), locator=Locators.password_locator)
        self.confirm_password = InputElement(driver=Browser.get_driver(), locator=Locators.confirm_password_locator)
        self.register_button = ButtonElement(driver=Browser.get_driver(), locator=Locators.register_button_locator)

    # def signup(self, user: User):
    #     LOGGER.info("Начинаем регистрацию")
    #     self.company_email.enter_text(user.company_email)
    #     self.first_name.enter_text(user.first_name)
    #     self.last_name.enter_text(user.last_name)
    #     self.company.enter_text(user.company)
    #     self.signup_button.key_code()
    #     LOGGER.info("Регистрация завершена")

    def signup(self, user: User): #логика всей регистрации
        LOGGER.info('Start register')
        self.gender.click_element()
        self.first_name.enter_text(user.first_name)
        self.last_name.enter_text(user.last_name)
        self.email.enter_text(user.email)
        self.password.enter_text(user.password)
        self.confirm_password.enter_text(user.confirm_password)
        self.register_button.click_element()
        LOGGER.info("Registration has just been finished")


from selenium import webdriver
from selenium.webdriver.common.by import By
from Automation.mainlogic.element import Element, InputElement, ButtonElement
from Automation.mainlogic.locators import Locators
from Automation.browser_chrome import Browser
import logging

LOGGER = logging.getLogger(__name__)

class Random: #выдаёт номера элементов в наличии из которых будет выбираться случайный для теста
    def __init__(self, Browser, grid, count_of_divs, in_stock_items, path_of_button):
        self.grid = InputElement(driver=Browser.get_driver(), locator=Locators.path_of_items)
        self.count_of_divs = len(grid.find_elements(By.XPATH, "./div"))
        self.in_stock_items = []
        self.path_of_button = Locators.path_of_button
        for i in range(count_of_divs):
            path_of_item = (f'/html/body/div[4]/div[1]/div[4]/div[2]/div[2]/div[2]/div[3]/div[{i}]')
            try:
                Browser.go_to_site(SignUp.path).find_element(By.XPATH, path_of_item+path_of_button).get_attribute('value') != 'Add to cart'
            except:
                in_stock_items.append(i)
class User:
    def __init__(self, gender, email, first_name, last_name, password, confirm_password):
        self.gender = gender
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.confirm_password = confirm_password




class SignUp():
    path = '/books'
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

    def signup(self, user: User): #шаги проверки бизнес логики
        LOGGER.info('Start buying')
        self.gender.click_element()
        self.first_name.enter_text(user.first_name)
        self.last_name.enter_text(user.last_name)
        self.email.enter_text(user.email)
        self.password.enter_text(user.password)
        self.confirm_password.enter_text(user.confirm_password)
        self.register_button.click_element()
        LOGGER.info("Buying has just been finished")


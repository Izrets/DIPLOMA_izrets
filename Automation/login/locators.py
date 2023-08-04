from selenium.webdriver.common.by import By


class Locators:
    email_locator = (By.ID, 'Email')
    password_locator = (By.NAME, 'Password')
    login_button_locator = (By.XPATH, '/html/body/div[4]/div[1]/div[4]/div[2]/div/div[2]/div[1]/div[2]/div[2]/form/div[5]/input')

from selenium.webdriver.common.by import By


class Locators:
    user_gender_m_locator = (By.ID, 'gender-male')
    user_gender_w_locator = (By.ID, 'gender-female')
    first_name_locator = (By.ID, 'FirstName')
    last_name_locator = (By.ID, 'LastName')
    email_locator = (By.ID, 'Email')

    password_locator = (By.NAME, 'Password')
    confirm_password_locator = (By.NAME, 'ConfirmPassword')

    register_button_locator = (By.NAME, 'register-button')

from selenium.webdriver.common.by import By

class Locators:
    cart_locator = (By.CLASS_NAME, 'cart-label')
    term_of_service_locator = (By.ID, 'termsofservice')
    checkout_locator = (By.ID, 'checkout')
    continuee_locator = (By.XPATH, '//*[@id="billing-buttons-container"]/input')
    in_store_locator = (By.XPATH, '//*[@id="PickUpInStore"]')
    COD_locator = (By.XPATH, '//*[@id="paymentmethod_0"]')
    ground_shipping_locator = (By.XPATH, '//*[@id="billing-buttons-container"]/input')
    continue_shipping_locator = (By.XPATH, '//*[@id="shipping-method-buttons-container"]/input')
    cash_locator = (By.XPATH, '//*[@id="checkout-payment-method-load"]/div/div/ul/li[1]/div/div[2]/label')
    continuee_in_store_locator = (By.XPATH, '//*[@id="shipping-buttons-container"]/input')
    continue_cod_locator = (By.XPATH, '//*[@id="payment-method-buttons-container"]/input')
    confirm_locator = (By.XPATH, '//*[@id="confirm-order-buttons-container"]/input')
    payment_info_continue_locator = (By.XPATH, '//*[@id="payment-info-buttons-container"]/input')

    email_locator = (By.ID, 'Email')
    password_locator = (By.NAME, 'Password')
    login_button_locator = (By.XPATH, '/html/body/div[4]/div[1]/div[4]/div[2]/div/div[2]/div[1]/div[2]/div[2]/form/div[5]/input')
    #/html/body/div[4]/div[1]/div[4]/div/div/div[2]/div/div[1]/strong Your order has been successfully processed!





#_________________________
    path_of_grid = (By.XPATH, '/html/body/div[4]/div[1]/div[4]/div[2]/div[2]/div[2]/div[3]')
    path_of_button = '/div/div[2]/div[3]/div[2]/input'

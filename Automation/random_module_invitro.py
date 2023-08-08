from selenium import webdriver
from selenium.webdriver.common.by import By
from random import randint
driver = webdriver.Chrome()
url = 'https://demowebshop.tricentis.com/books'
driver.get(url)

# List<WebElement> forms = driver.findElements(By.cssSelector(".product_row form"));
# int count = forms.size();
# grid = driver.find_element(By.CSS_SELECTOR, '.product-grid')

grid = driver.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[4]/div[2]/div[2]/div[2]/div[3]')
# count_of_divs = len(grid.find_elements(By.XPATH, "./div"))
# for i in grid:
#     count = 0
count_of_divs = len(grid.find_elements(By.XPATH, "./div"))
in_stock_items = []
path_of_button = '/div/div[2]/div[3]/div[2]/input'
for i in range(count_of_divs):
    path_of_item = (f'/html/body/div[4]/div[1]/div[4]/div[2]/div[2]/div[2]/div[3]/div[{i}]')
    try:
        driver.find_element(By.XPATH, path_of_item+path_of_button).get_attribute('value') != 'Add to cart'
    except:
        in_stock_items.append(i)
print(in_stock_items)
#random click

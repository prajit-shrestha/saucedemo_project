from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage:
    def __init__(self,driver):
        self.driver = driver

        self.add_to_cart = (By.ID, 'add-to-cart-sauce-labs-backpack')
        self.click_shopping_icon = (By.CLASS_NAME, 'shopping_cart_link')

    def add_product_to_cart(self):
        self.driver.find_element(*self.add_to_cart).click()

    def go_to_shopping_cart(self):
        self.driver.find_element(*self.click_shopping_icon).click()


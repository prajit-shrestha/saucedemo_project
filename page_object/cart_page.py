from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class CartPage:
    def __init__(self,driver):
        self.driver = driver

        self.checkout = (By.ID, 'checkout')

    def click_checkout(self):
        self.driver.find_element(*self.checkout).click()
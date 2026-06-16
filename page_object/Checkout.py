from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

        self.firstname = (By.ID, "first-name")
        self.lastname = (By.ID, "last-name")
        self.zipcode = (By.ID, "postal-code")
        self.continue_btn = (By.ID, "continue")

    def enter_firstname(self, fname):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.firstname)
        )
        element.clear()
        element.send_keys(fname)

    def enter_lastname(self, lname):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.lastname)
        )
        element.clear()
        element.send_keys(lname)

    def enter_zipcode(self, code):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.zipcode)
        )
        element.clear()
        element.send_keys(code)

    def click_continue(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.continue_btn)
        ).click()

    def checkout_details(self, fname, lname, code):
        self.enter_firstname(fname)
        self.enter_lastname(lname)
        self.enter_zipcode(code)
        self.click_continue()
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class LoginPage:
    def __init__(self,driver):
        self.driver = driver

        # Locator
        self.username = (By.XPATH, "//input[@id='user-name']")
        self.password = (By.XPATH, "//input[@id='password']")
        self.login_btn = (By.XPATH, "//input[@id='login-button']")

    def enter_username(self,username):
        wait = WebDriverWait(self.driver,10)
        wait.until(EC.visibility_of_element_located(self.username)).send_keys(username)

    def enter_password(self,password):
        wait = WebDriverWait(self.driver,10)
        wait.until(EC.visibility_of_element_located(self.password)).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_btn).click()

    def login(self,username,password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()


from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class LogoutPage:
    def __init__(self,driver):
        self.driver = driver

        self.menu_btn = (By.ID,"react-burger-menu-btn")
        self.logout_btn = (By.ID,"logout_sidebar_link")

    def click_menu(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.menu_btn))
        self.driver.find_element(*self.menu_btn).click()

    def click_logout(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.logout_btn))
        self.driver.find_element(*self.logout_btn).click()

    def logout(self):
        self.click_menu()
        self.click_logout()



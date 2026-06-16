from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutCompletePage:
    def __init__(self,driver):
        self.driver = driver

        self.finish_btn = (By.ID,'finish')
        self.thank_you_text = (By.CLASS_NAME, "complete-header")

    def click_finish_btn(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located(self.finish_btn)).click()

    def get_thank_you_text(self):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(
            EC.visibility_of_element_located(self.thank_you_text)
        ).text
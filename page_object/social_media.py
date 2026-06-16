from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class SocialMedia():
    def __init__(self,driver):
        self.driver = driver
        self.tweeter = (By.XPATH,"//a[normalize-space()='Twitter']")
        self.facebook = (By.XPATH,"//a[normalize-space()='Facebook']")
        self.linkdin = (By.XPATH,"//a[normalize-space()='LinkedIn']")

    def get_twitter(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.tweeter)).click()

    def get_facebook(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.facebook)).click()

    def get_linkdin(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.linkdin)).click()

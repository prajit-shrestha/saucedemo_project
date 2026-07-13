import pytest
from page_object.login_page import LoginPage
from config.config import BASE_URL, USERNAME, PASSWORD, Inventory_url
from utilities.logger import get_logger

logger = get_logger()
def test_login(driver):
    driver.get(BASE_URL)
    logger.info("Starting login test")
    login = LoginPage(driver)
    login.enter_username(USERNAME)
    login.enter_password(PASSWORD)
    login.click_login()

    url = "https://www.saucedemo.com/inventory.html"
    assert driver.current_url == url

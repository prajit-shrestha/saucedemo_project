import pytest
from page_object.login_page import LoginPage
from config.config import BASE_URL, USERNAME, PASSWORD, Inventory_url
from utilities.logger import get_logger
import allure

logger = get_logger()

@allure.title("Verify valid user login")
@allure.description("Verify user can login successfully with valid credentials")
def test_login(driver):
    driver.get(BASE_URL)
    logger.info("Starting login test")
    login = LoginPage(driver)
    with allure.step("Enter username"):
        login.enter_username(USERNAME)

    with allure.step("Enter password"):
        login.enter_password(PASSWORD)
    with allure.step("Click login button"):
        login.click_login()
    with allure.step("Verify user is redirected to inventory page"):
        url = "inventory.html"
    assert url in driver.current_url

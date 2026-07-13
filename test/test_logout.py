from page_object import login_page
from page_object.login_page import LoginPage
from page_object.logout import LogoutPage
from config.config import BASE_URL,USERNAME,PASSWORD
from utilities.logger import get_logger

logger = get_logger()

def test_logout(driver):
    driver.get(BASE_URL)

    login = LoginPage(driver)
    login.login(USERNAME,PASSWORD)

    logger.info("Starting logout test")
    logout = LogoutPage(driver)
    logger.info("Clicked logout")
    logout.logout()
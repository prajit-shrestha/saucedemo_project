from page_object.login_page import LoginPage
from config.config import BASE_URL,USERNAME,PASSWORD

def test_login(driver):
    driver.get(BASE_URL)

    login = LoginPage(driver)
    login.login(USERNAME,PASSWORD)

    assert "https://www.saucedemo.com/inventory.html" in driver.current_url
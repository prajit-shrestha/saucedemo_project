from selenium.webdriver.common.by import By
from page_object.login_page import LoginPage
from page_object.Inventorypage import InventoryPage
from page_object.Checkout import CheckoutPage
from page_object.cart_page import CartPage
from config.config import BASE_URL, USERNAME, PASSWORD
from utilities.logger import get_logger

logger = get_logger()


def test_checkout(driver):
    # Open website
    driver.get(BASE_URL)

    # Login
    login = LoginPage(driver)
    login.login(USERNAME, PASSWORD)

    # Inventory Page
    logger.info("Starting inventory test")
    inventory = InventoryPage(driver)
    inventory.add_product_to_cart()
    inventory.go_to_shopping_cart()

    # Cart Page
    cartpage = CartPage(driver)
    cartpage.click_checkout()

    print("After checkout click:", driver.current_url)

    # Checkout Information Page
    logger.info("Starting checkout test")
    checkout = CheckoutPage(driver)
    logger.info("Adding details")
    checkout.checkout_details("prajit", "shrestha", "44600")


    # Assertion
    title = driver.find_element(By.CLASS_NAME, "title")

    assert title.text == "Checkout: Overview", \
        f"Expected 'Checkout: Overview' but got '{title.text}'"
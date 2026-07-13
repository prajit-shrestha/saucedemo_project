from conftest import driver
from page_object.login_page import LoginPage
from page_object.Inventorypage import InventoryPage
from page_object.cart_page import CartPage
from page_object.Checkout import CheckoutPage
from page_object.checkout_complete import CheckoutCompletePage
from config.config import BASE_URL,USERNAME,PASSWORD
from utilities.logger import get_logger

logger = get_logger()


def test_checkout_complete(driver):
    driver.get(BASE_URL)

    #login
    login = LoginPage(driver)
    login.login(USERNAME,PASSWORD)

    #inventory
    inventory = InventoryPage(driver)
    inventory.add_product_to_cart()
    inventory.go_to_shopping_cart()

    #Cart
    cart = CartPage(driver)
    cart.click_checkout()

    #Checkout information page
    checkout = CheckoutPage(driver)
    checkout.checkout_details("Prajit", "shrestha", "44600")

    #Checkout finish page
    checkout_complete = CheckoutCompletePage(driver)
    checkout_complete.click_finish_btn()

    #asseertion
    thank_you = checkout_complete.get_thank_you_text()
    assert "THANK YOU FOR YOUR ORDER" in thank_you.upper()




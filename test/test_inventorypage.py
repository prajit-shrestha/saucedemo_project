from selenium.webdriver.common.by import By
from page_object.Inventorypage import InventoryPage
from page_object.login_page import LoginPage
from config.config import BASE_URL, USERNAME, PASSWORD
from utilities.logger import get_logger

logger = get_logger()

def test_add_to_cart(driver):
    driver.get(BASE_URL)

    login = LoginPage(driver)
    login.login(USERNAME, PASSWORD)

    #Inventory page
    logger.info("Starting inventory test")
    inventory = InventoryPage(driver)

    #add to cart
    logger.info("Adding the product")
    inventory.add_product_to_cart()

    #add to shopping cart
    logger.info("Navigate to shopping cart")
    inventory.go_to_shopping_cart()

    cart_item = driver.find_element(By.XPATH,"//div[@class='cart_quantity']" )
    assert "cart_item.is_displayed()" ,"Cart items are not displayed"


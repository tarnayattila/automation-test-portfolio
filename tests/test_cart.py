from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

def test_add_to_cart(driver):

    login = LoginPage(driver)
    inventory = InventoryPage(driver)
    cart = CartPage(driver)

    login.open()
    login.login("standard_user", "secret_sauce")

    assert "inventory" in driver.current_url

    inventory.add_backpack()
    inventory.add_bike_light()
    inventory.open_cart()
    cart.remove_first_item()
    cart.get_cart_count()
    assert cart.get_cart_count() == "1"
    cart.start_checkout()

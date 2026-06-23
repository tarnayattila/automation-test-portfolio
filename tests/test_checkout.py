from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.checkout_page import CheckoutPage
from pages.cart_page import CartPage
import json

with open("data/checkout_data.json") as f:
    checkout_data = json.load(f)

def test_checkout(driver):

    login = LoginPage(driver)
    inventory = InventoryPage(driver)
    cart = CartPage(driver)
    checkout = CheckoutPage(driver)

    login.open()
    login.login("standard_user", "secret_sauce")

    assert "inventory" in driver.current_url

    inventory.add_backpack()
    inventory.add_bike_light()
    inventory.open_cart()
    cart.remove_bike_light()
    cart.get_cart_count()
    assert cart.get_cart_count() == "1"

    cart.start_checkout()

    checkout.fill_info(
        checkout_data["first_name"],
        checkout_data["last_name"],
        checkout_data["zip_code"]
    )

    checkout.continue_checkout()
    checkout.finish_checkout()
    success_msg = checkout.get_success_message()
    assert success_msg == "Thank you for your order!"


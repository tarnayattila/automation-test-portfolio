import allure
from core.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage(BasePage):

    ADD_BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")
    ADD_BIKE_LIGHT = (By.ID, "add-to-cart-sauce-labs-bike-light")

    REMOVE_BACKPACK = (By.ID, "remove-sauce-labs-backpack")
    REMOVE_BIKE_LIGHT = (By.ID, "remove-sauce-labs-bike-light")

    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")

    @allure.step("Add Backpack")
    def add_backpack(self):
        self.click(self.ADD_BACKPACK)

    @allure.step("Add Bike Light")
    def add_bike_light(self):
        self.click(self.ADD_BIKE_LIGHT)

    @allure.step("Remove Backpack")
    def remove_backpack(self):
        self.click(self.REMOVE_BACKPACK)

    @allure.step("Remove Bike Light")
    def remove_bike_light(self):
        self.click(self.REMOVE_BIKE_LIGHT)

    @allure.step("Open cart")
    def open_cart(self):
        self.click(self.CART_ICON)
        self.wait.until(lambda d: "/cart" in d.current_url)
        self.wait.until(
            EC.presence_of_element_located((By.ID, "cart_contents_container"))
        )
    def get_cart_count(self):
        try:
            return self.get_text(self.CART_BADGE)
        except:
            return "0"
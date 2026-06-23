import allure
from core.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class CartPage(BasePage):

    CHECKOUT = (By.ID, "checkout")
    CART_ITEM = (By.CLASS_NAME, "cart_item")
    REMOVE_BTN = (By.CLASS_NAME, "cart_button")

    REMOVE_BACKPACK = (By.ID, "remove-sauce-labs-backpack")
    REMOVE_BIKE_LIGHT = (By.ID, "remove-sauce-labs-bike-light")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")

    def get_items(self):
        return self.driver.find_elements(*self.CART_ITEM)

    def get_items_count(self):
        return len(self.get_items())

    def remove_first_item(self):
        items = self.get_items()
        if items:
            items[0].find_element(By.CLASS_NAME, "cart_button").click()

    @allure.step("Remove Backpack")
    def remove_backpack(self):
        self.click(self.REMOVE_BACKPACK)

    @allure.step("Remove Bike Light")
    def remove_bike_light(self):
        self.click(self.REMOVE_BIKE_LIGHT)

    def get_cart_count(self):
        try:
            return self.get_text(self.CART_BADGE)
        except:
            return "0"

    @allure.step("Start checkout")
    def start_checkout(self):
        self.debug_url("Current url: ")
        self.click(self.CHECKOUT)
        self.wait.until(
            EC.visibility_of_element_located(((By.ID, "checkout_info_container")))
                        )
        self.wait.until(lambda d: d.execute_script("return document.readyState") == "complete")
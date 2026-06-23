import allure
from core.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class CartPage(BasePage):

    CHECKOUT = (By.ID, "checkout")
    CART_ITEM = (By.CLASS_NAME, "cart_item")
    REMOVE_BTN = (By.CLASS_NAME, "cart_button")

    def get_items(self):
        return self.driver.find_elements(*self.CART_ITEM)

    def get_items_count(self):
        return len(self.get_items())

    def remove_first_item(self):
        items = self.get_items()
        if items:
            items[0].find_element(By.CLASS_NAME, "cart_button").click()

    @allure.step("Start checkout")
    def start_checkout(self):
        self.debug_url("Current url: ")
        self.click(self.CHECKOUT)
        self.wait.until(
            EC.visibility_of_element_located((By.ID, "checkout_info_container"))
        )
        self.wait.until(lambda d: d.execute_script("return document.readyState") == "complete")
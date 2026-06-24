import allure
from core.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage(BasePage):
    CART = (By.CLASS_NAME, "shopping_cart_link")
    CHECKOUT = (By.ID, "checkout")

    FIRST = (By.ID, "first-name")
    LAST = (By.ID, "last-name")
    ZIP = (By.ID, "postal-code")

    CONTINUE = (By.ID, "continue")
    FINISH = (By.ID, "finish")

    SUCCESS = (By.CSS_SELECTOR, "[data-test='complete-header']")
    ERROR = (By.CLASS_NAME, "error-message-container")

    def open_cart(self):
        self.click(self.CART)

        self.is_visible(self.CHECKOUT)

    def start_checkout(self):
        self.click(self.CHECKOUT)
        return self.wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "step-one")))

    @allure.step("Fill checkout form")
    def fill_info(self, first, last, zip_code):
        self.wait.until(
            EC.url_contains("checkout-step-one")
        )
        assert "checkout-step-one" in self.driver.current_url
        self.wait.until(lambda d: d.execute_script("return document.readyState") == "complete")
        self.type_and_verify(self.FIRST, first)
        self.type_and_verify(self.LAST, last)
        self.type_and_verify(self.ZIP, zip_code)

        first_val = self.driver.find_element(*self.FIRST).get_attribute("value")
        last_val = self.driver.find_element(*self.LAST).get_attribute("value")
        zip_val = self.driver.find_element(*self.ZIP).get_attribute("value")

        print("FIRST:", first_val)
        print("LAST:", last_val)
        print("ZIP:", zip_val)

        print("FIRST VALUE:", self.driver.find_element(By.ID, "first-name").get_attribute("value"))
        print("LAST VALUE:", self.driver.find_element(By.ID, "last-name").get_attribute("value"))
        print("ZIP VALUE:", self.driver.find_element(By.ID, "postal-code").get_attribute("value"))

        assert first_val == first
        assert last_val == last
        assert zip_val == zip_code


    @allure.step("Continue checkout")
    def continue_checkout(self):
        self.debug_url("Current url: ")
        self.driver.execute_script("document.activeElement.blur();")
        self.click(self.CONTINUE)
        self.wait.until(
            lambda d: (
                    len(d.find_elements(By.ID, "checkout_summary_container")) > 0
                    or len(d.find_elements(By.CLASS_NAME, "error-message-container")) > 0
            )
        )

        errors = self.driver.find_elements(By.CLASS_NAME, "error-message-container")

        if errors and errors[0].text.strip():
            raise AssertionError(f"Checkout failed: {errors[0].text}")

    @allure.step("Finish checkout")
    def finish_checkout(self):
        print("NOW ON STEP TWO:", self.driver.current_url)
        self.wait.until(
            EC.visibility_of_element_located(self.FINISH)
        )
        self.click(self.FINISH)
        self.wait.until(
            EC.visibility_of_element_located(self.SUCCESS)
        )
        assert self.is_visible(self.SUCCESS)


    @allure.step("Successful checkout")
    def get_success_message(self):
        return self.driver.find_element(*self.SUCCESS).text
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
        return self.wait.until(
            EC.url_contains("checkout-step-one")
        )

    @allure.step("Fill checkout form")
    def fill_info(self, first, last, zip_code):
        self.type_and_verify(self.FIRST, first)
        self.type_and_verify(self.LAST, last)
        self.type_and_verify(self.ZIP, zip_code)

        first_val = self.driver.find_element(*self.FIRST).get_attribute("value")
        last_val = self.driver.find_element(*self.LAST).get_attribute("value")
        zip_val = self.driver.find_element(*self.ZIP).get_attribute("value")

        print("FIRST:", first_val)
        print("LAST:", last_val)
        print("ZIP:", zip_val)

        print("FIRST visible:",
              self.driver.find_element(*self.FIRST).is_displayed())

        print("FIRST enabled:",
              self.driver.find_element(*self.FIRST).is_enabled())

        print("LAST visible:",
              self.driver.find_element(*self.LAST).is_displayed())

        print("LAST enabled:",
              self.driver.find_element(*self.LAST).is_enabled() )

        print("ZIP visible:",
              self.driver.find_element(*self.ZIP).is_displayed())

        print("ZIP enabled:",
              self.driver.find_element(*self.ZIP).is_enabled())

        print("FIRST VALUE:", self.driver.find_element(By.ID, "first-name").get_attribute("value"))
        print("LAST VALUE:", self.driver.find_element(By.ID, "last-name").get_attribute("value"))
        print("ZIP VALUE:", self.driver.find_element(By.ID, "postal-code").get_attribute("value"))

        assert first_val == first
        assert last_val == last
        assert zip_val == zip_code
        self.wait.until(
            EC.presence_of_element_located(
                (By.ID, "continue")
            )
        )

    @allure.step("Continue checkout")
    def continue_checkout(self):
        self.debug_url("Current url: ")
        self.click(self.CONTINUE)

        self.wait.until(
            EC.presence_of_element_located(
                (By.ID, "checkout_summary_container")
            )
        )

        print("NOW ON STEP TWO:", self.driver.current_url)

    @allure.step("Finish checkout")
    def finish_checkout(self):
        self.click(self.FINISH)

        self.wait.until(
            EC.visibility_of_element_located(self.SUCCESS)
        )
        assert self.is_visible(self.SUCCESS)


    @allure.step("Successful checkout")
    def get_success_message(self):
        return self.driver.find_element(*self.SUCCESS).text
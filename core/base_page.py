from pydoc import text

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import ElementClickInterceptedException

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def wait_for_input_ready(self, locator):
        self.wait.until(EC.presence_of_element_located(locator))
        self.wait.until(EC.visibility_of_element_located(locator))
        self.wait.until(EC.element_to_be_clickable(locator))

        return self.driver.find_element(*locator)

    def click(self, locator):
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", element)

        self.wait.until(EC.visibility_of(element))
        self.wait.until(EC.element_to_be_clickable(locator))

        try:
            element.click()
        except:
            self.driver.execute_script("arguments[0].click();", element)

    def safe_click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self.driver.execute_script("arguments[0].click();", element)

    def type(self, locator, text,):

                element = self.wait.until(EC.visibility_of_element_located(locator))

                self.driver.execute_script(
                    "arguments[0].scrollIntoView({block: 'center'});",
                    element
                )

                element.click()
                element.clear()

                element.send_keys(text)
                self.wait.until(lambda d: len(d.find_element(*locator).get_attribute("value")) >= len(text) - 1)

    def type_and_verify(self, locator, text):
        self.type(locator, text)

    def get_text(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    def is_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).is_displayed()

    def wait_for_disappear(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element_located(locator)
        )

    def debug_url(self, label="URL"):
        print(f"[{label}] {self.driver.current_url}")
        return self.driver.current_url
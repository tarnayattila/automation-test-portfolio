from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException
import time

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
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

        try:
            self.wait.until(EC.element_to_be_clickable(locator))
            element.click()
        except ElementClickInterceptedException:
            self.driver.execute_script("arguments[0].click();", element)

    def type(self, locator, text, retries=2):
        last_exception = None

        for _ in range(retries):
            try:
                element = self.wait.until(EC.visibility_of_element_located(locator))

                self.driver.execute_script(
                    "arguments[0].scrollIntoView({block: 'center'});",
                    element
                )

                element.click()
                element.clear()

                element.send_keys(text,"\t")

                value = element.get_attribute("value")

                if value == text:
                    return

                self.driver.execute_script("""
                    arguments[0].value = arguments[1];
                    arguments[0].dispatchEvent(new Event('input', { bubbles: true }));
                    arguments[0].dispatchEvent(new Event('change', { bubbles: true }));
                """, element, text)

                value = element.get_attribute("value")

                if value == text:
                    return

            except Exception as e:
                last_exception = e
                time.sleep(0.3)

        raise Exception(f"Type failed for {locator}: {text}") from last_exception

    def type_and_verify(self, locator, text):
        self.type(locator, text)

        value = self.driver.find_element(*locator).get_attribute("value")

        if value != text:
            self.driver.execute_script(
                "arguments[0].value = arguments[1]; arguments[0].dispatchEvent(new Event('input', {bubbles:true}));",
                self.driver.find_element(*locator),
                text
            )

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
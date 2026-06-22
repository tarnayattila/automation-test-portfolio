from selenium.webdriver.support.ui import WebDriverWait

def wait_for_url(driver, part, timeout=10):
    WebDriverWait(driver, timeout).until(
        lambda d: part in d.current_url
    )
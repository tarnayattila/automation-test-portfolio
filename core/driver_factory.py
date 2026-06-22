from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FFOptions
from core.config import Config


def create_driver():
    browser = Config.BROWSER

    if browser == "chrome":
        options = Options()
        if Config.HEADLESS:
            options.add_argument("--headless=new")
        options.add_argument("--window-size=1920,1080")

        driver = webdriver.Chrome(options=options)

    elif browser == "firefox":
        options = FFOptions()
        if Config.HEADLESS:
            options.add_argument("--headless")

        driver = webdriver.Firefox(options=options)

    else:
        raise Exception("Unsupported browser")

    driver.implicitly_wait(0)
    return driver
import os

class Config:
    BASE_URL = "https://www.saucedemo.com"
    BROWSER = os.getenv("BROWSER", "chrome")
    HEADLESS = os.getenv("HEADLESS", "true") == "true"
    TIMEOUT = 10
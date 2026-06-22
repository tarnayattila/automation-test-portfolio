import allure
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage

def test_invalid_login(driver):

    login = LoginPage(driver)
    login.open()

    login.login("invalid_user", "wrong_password")

    error = driver.find_element(By.CLASS_NAME, "error-message-container")

    assert "Epic sadface" in error.text
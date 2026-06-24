import allure
from core.base_page import BasePage
from core.config import Config

class LoginPage(BasePage):

    USERNAME = ("id", "user-name")
    PASSWORD = ("id", "password")
    LOGIN_BTN = ("id", "login-button")

    def open(self):
        self.driver.get(Config.BASE_URL)

    @allure.step("Login with user: {user} and password: {password}")
    def login(self, user, password):
        self.type(self.USERNAME, user)
        self.type(self.PASSWORD, password)
        self.click(self.LOGIN_BTN)

    def get_error_message(self):
        return self.get_text(self.ERROR)
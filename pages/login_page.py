from playwright.sync_api import Page
from .base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.username_textbox = page.locator("#user-name")
        self.password_textbox = page.locator("#password")
        self.login_button = page.locator("#login-button")
        self.error_message = page.locator(".error-message-container.error")

    def goto_login_page(self):
        self.open("https://www.saucedemo.com")

    def fill_username(self, username):
        self.username_textbox.fill(username)

    def fill_password(self, password):
        self.password_textbox.fill(password)

    def click_login(self):
        self.login_button.click()

    def login(self, username, password):
        self.fill_username(username)
        self.fill_password(password)
        self.click_login()

    def get_error_message(self):
        return self.error_message.text_content()

    def is_error_displayed(self):
        return self.error_message.is_visible()
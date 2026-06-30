import json

from playwright.sync_api import expect
from playwright.sync_api._generated import Page
from pages.login_page import LoginPage

# Đọc file JSON
with open("test_data/users.json", "r", encoding="utf-8") as file:
    users = json.load(file)


class TestLogin:
 def test_login_success(self, page: Page):
  login = LoginPage(page)
  login.goto_login_page()
  login.login(users["validUser"]["username"], users["validUser"]["password"])
  expect(page).to_have_url("https://www.saucedemo.com/inventory.html")


 def test_login_invalid_password(self, page: Page):
  login = LoginPage(page)
  login.goto_login_page()
  login.login(users["invalidPassword"]["username"],users["invalidPassword"]["password"])
  expect(login.error_message).to_be_visible()
  assert "Epic sadface: Username and password do not match any user in this service" in login.get_error_message()
 
 def test_login_invalid_username(self, page):
  login = LoginPage(page)
  login.goto_login_page()
  login.login(users["invalidUsername"]["username"],users["invalidUsername"]["password"])
  expect(login.error_message).to_be_visible()
  assert "Epic sadface: Username and password do not match any user in this service" in login.get_error_message()

 def test_login_empty_username_password(self, page):
  login = LoginPage(page)
  login.goto_login_page()
  login.login(users["emptyUser"]["username"],users["emptyUser"]["password"])
  expect(login.error_message).to_be_visible()
  assert "Epic sadface: Username is required" in login.get_error_message()
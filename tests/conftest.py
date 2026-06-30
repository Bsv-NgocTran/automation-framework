import json
import pytest
from playwright.sync_api import Page

from pages.login_page import LoginPage

# Đọc file JSON
with open("test_data/users.json", "r", encoding="utf-8") as file:
    users = json.load(file)



@pytest.fixture
def logged_in_page(page):
    """Đăng nhập bằng valid user và trả về page"""

    login = LoginPage(page)
    login.goto_login_page()
    login.login(users["validUser"]["username"],users["validUser"]["password"])
    return page
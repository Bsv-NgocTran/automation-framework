from playwright.sync_api import Page
from .base_page import BasePage


class CartPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.continue_shopping_button = page.locator("#continue-shopping")
        self.checkout_button = page.locator("#checkout")
        self.cart_items = page.locator(".cart_item")
        self.product_names = page.locator(".inventory_item_name")
        self.product_prices = page.locator(".inventory_item_price")
        self.remove_backpack_button = page.locator("#remove-sauce-labs-backpack")


    def continue_shopping(self):
        self.continue_shopping_button.click()

    def checkout(self):
        self.checkout_button.click()

    def remove_backpack(self):
        self.remove_backpack_button.click()

    def get_cart_item_count(self):
        return self.cart_items.count()

    def get_product_name(self, index=0):
        return self.product_names.nth(index).text_content()

    def get_product_price(self, index=0):
        return self.product_prices.nth(index).text_content()

    def is_checkout_button_visible(self):
        return self.checkout_button.is_visible()

    def is_continue_shopping_visible(self):
        return self.continue_shopping_button.is_visible()

    def is_remove_button_visible(self):
        return self.remove_backpack_button.is_visible()

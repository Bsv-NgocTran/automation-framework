from playwright.sync_api import Page
from .base_page import BasePage


class ProductPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.shopping_cart = page.locator(".shopping_cart_link")
        self.menu_button = page.locator("#react-burger-menu-btn")
        self.sort_dropdown = page.locator(".product_sort_container")
        self.product_list = page.locator(".inventory_item")
        self.product_names = page.locator(".inventory_item_name")
        self.product_prices = page.locator(".inventory_item_price")
        self.product_descriptions = page.locator(".inventory_item_desc")
        self.backpack_name = page.locator("#item_4_title_link")
        self.add_backpack = page.locator("#add-to-cart-sauce-labs-backpack")
        self.remove_backpack = page.locator("#remove-sauce-labs-backpack")

    def goto_inventory_page(self):
        self.open("https://www.saucedemo.com/inventory.html")

    def click_backpack(self):
        self.backpack_name.click()

    def add_backpack_to_cart(self):
        self.add_backpack.click()

    def remove_backpack_from_cart(self):
        self.remove_backpack.click()

    def open_cart(self):
        self.shopping_cart.click()

    def get_product_count(self):
        return self.product_list.count()

    def get_product_name(self, index):
        return self.product_names.nth(index).text_content()

    def get_product_price(self, index):
        return self.product_prices.nth(index).text_content()

    def is_cart_visible(self):
        return self.shopping_cart.is_visible()
    
    def is_add_button_visible(self):
        return self.add_backpack.is_visible()

    def is_remove_button_visible(self):
        return self.remove_backpack.is_visible()
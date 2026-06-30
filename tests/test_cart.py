from playwright.sync_api import expect

from pages.product_page import ProductPage
from pages.cart_page import CartPage


class TestCart:

    def test_add_product_to_cart(self, logged_in_page):
     product = ProductPage(logged_in_page)
     cart = CartPage(logged_in_page)
     product.add_backpack_to_cart()
     product.open_cart()
     expect(logged_in_page).to_have_url("https://www.saucedemo.com/cart.html")
     assert cart.get_cart_item_count() == 1
     assert cart.get_product_name() == "Sauce Labs Backpack"
     assert cart.get_product_price() == "$29.99"
     assert cart.is_remove_button_visible()


    def test_remove_product_from_cart(self, logged_in_page):
     product = ProductPage(logged_in_page)
     cart = CartPage(logged_in_page)
     product.add_backpack_to_cart()
     product.open_cart()
     cart.remove_backpack()
     assert cart.get_cart_item_count() == 0


    def test_checkout_button_visible(self, logged_in_page):
     product = ProductPage(logged_in_page)
     cart = CartPage(logged_in_page)
     product.open_cart()
     assert cart.is_checkout_button_visible()


    def test_continue_shopping_button_visible(self, logged_in_page):
     product = ProductPage(logged_in_page)
     cart = CartPage(logged_in_page)
     product.open_cart()
     assert cart.is_continue_shopping_visible()


    def test_continue_shopping(self, logged_in_page):
     product = ProductPage(logged_in_page)
     cart = CartPage(logged_in_page)
     product.open_cart()
     cart.continue_shopping()
     expect(logged_in_page).to_have_url("https://www.saucedemo.com/inventory.html")


    def test_checkout(self, logged_in_page):
     product = ProductPage(logged_in_page)
     cart = CartPage(logged_in_page)
     product.add_backpack_to_cart()
     product.open_cart()
     cart.checkout()
     expect(logged_in_page).to_have_url("https://www.saucedemo.com/checkout-step-one.html")
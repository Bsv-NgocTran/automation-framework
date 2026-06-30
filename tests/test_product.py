from playwright.sync_api import expect

from pages.product_page import ProductPage


class TestProduct:

    def test_display_product_list(self, logged_in_page):
     product = ProductPage(logged_in_page)
     expect(logged_in_page).to_have_url("https://www.saucedemo.com/inventory.html")
     
    def test_cart_icon_visible(self, logged_in_page):
     product = ProductPage(logged_in_page)
     assert product.is_cart_visible()

    def test_product_name(self, logged_in_page):
     product = ProductPage(logged_in_page)
     assert product.get_product_name(0) == "Sauce Labs Backpack"

    def test_product_price(self, logged_in_page):
     product = ProductPage(logged_in_page)
     assert product.get_product_price(0) == "$29.99"

    def test_view_product_detail(self, logged_in_page):
     product = ProductPage(logged_in_page)
     product.click_backpack()
     expect(logged_in_page).to_have_url("https://www.saucedemo.com/inventory-item.html?id=4")
   
    def test_add_product_to_cart(self, logged_in_page):
     product = ProductPage(logged_in_page)
     product.add_backpack_to_cart()
     assert product.is_remove_button_visible()

    def test_remove_product_from_cart(self, logged_in_page):
     product = ProductPage(logged_in_page)
     product.add_backpack_to_cart()
     product.remove_backpack_from_cart()
     assert product.is_add_button_visible()
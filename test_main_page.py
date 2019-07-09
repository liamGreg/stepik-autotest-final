from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.cart_page import CartPage


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()
    page.go_to_login_page()

    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

def test_guest_cant_see_product_in_cart_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_cart_link()
    page.go_to_cart_page()

    cart = CartPage(browser, browser.current_url)
    cart.should_not_be_cart_items()
    cart.should_be_cart_is_empty_text()

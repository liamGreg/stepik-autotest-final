from .base_page import BasePage
from .locators import CartPageLocators


class CartPage(BasePage):
    def should_not_be_cart_items(self):
        assert self.is_not_element_present(
            *CartPageLocators.CART_ITEMS), "Cart items is presented, but should not be."

    def should_be_cart_is_empty_text(self):
        assert self.is_element_present(*CartPageLocators.CART_IS_EMPTY), "Cart is not empty."

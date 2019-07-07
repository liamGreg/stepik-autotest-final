from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_item_to_basket(self):
        self.should_be_add_to_basket_button()
        self.click_add_to_basket_button()
        self.solve_quiz_and_get_code()

        title = self.get_item_title()
        self.should_be_success_alert_of_added_item(title)

        price = self.get_item_price()
        self.should_be_item_price_and_basket_total_equal(price)

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(
            *ProductPageLocators.ADD_TO_BASKET_BUTTON), "Add to basket button is not presented."

    def click_add_to_basket_button(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()

    def get_item_title(self):
        assert self.is_element_present(*ProductPageLocators.ITEM_TITLE), "Item's title is not presented."
        return self.browser.find_element(*ProductPageLocators.ITEM_TITLE).text

    def should_be_success_alert_of_added_item(self, title):
        assert self.is_element_present(
            *ProductPageLocators.ITEM_ADDED_TO_BASKET_SUCCESS_ALERT), "There is no success alerts presented."
        assert self.browser.find_element(
            *ProductPageLocators.ITEM_ADDED_TO_BASKET_SUCCESS_ALERT).text == title, "Current item is not added to basket."

    def should_be_basket_total_alert(self):
        assert self.is_element_present(
            *ProductPageLocators.BASKET_TOTAL_INFO_ALERT), "There is no basket total info alert presented."

    def get_item_price(self):
        assert self.is_element_present(*ProductPageLocators.ITEM_PRICE), "Item's title is not presented."
        return self.browser.find_element(*ProductPageLocators.ITEM_PRICE).text

    def should_be_item_price_and_basket_total_equal(self, price):
        assert self.browser.find_element(
            *ProductPageLocators.BASKET_TOTAL_INFO_ALERT).text == price, "Item's price and basket's total is not equal."

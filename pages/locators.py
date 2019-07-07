from selenium.webdriver.common.by import By


class BasePageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class MainPageLocators(object):
    pass


class LoginPageLocators(object):
    LOGIN_URL_PART = "login"
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")


class ProductPageLocators(object):
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    ITEM_ADDED_TO_BASKET_SUCCESS_ALERT = (By.CSS_SELECTOR, ".alert-success:first-of-type strong")
    ITEM_TITLE = (By.CSS_SELECTOR, ".product_main h1")
    BASKET_TOTAL_INFO_ALERT = (By.CSS_SELECTOR, ".alert-info strong")
    ITEM_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")

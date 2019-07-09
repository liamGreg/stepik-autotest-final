from selenium.webdriver.common.by import By


class BasePageLocators(object):
    LOGIN_LINK = (By.ID, "login_link")
    LOGIN_LINK_INVALID = (By.ID, "login_link_inc")
    CART_LINK = (By.CSS_SELECTOR, "a.btn-default:not(.navbar-btn)[href$='/basket/']")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators(object):
    pass


class LoginPageLocators(object):
    LOGIN_URL_PART = "login"
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    REGISTER_EMAIL_INPUT = (By.ID, "id_registration-email")
    REGISTER_PASSWORD_INPUT = (By.ID, "id_registration-password1")
    REGISTER_PASSWORD_REPEAT_INPUT = (By.ID, "id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "#register_form button")


class ProductPageLocators(object):
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-cart")
    ITEM_ADDED_TO_CART_SUCCESS_ALERT = (By.CSS_SELECTOR, ".alert-success:first-of-type strong")
    ITEM_TITLE = (By.CSS_SELECTOR, ".product_main h1")
    CART_TOTAL_INFO_ALERT = (By.CSS_SELECTOR, ".alert-info strong")
    ITEM_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")


class CartPageLocators(object):
    CART_ITEMS = (By.CSS_SELECTOR, ".basket-items")
    CART_IS_EMPTY = (By.CSS_SELECTOR, "#content_inner > p")

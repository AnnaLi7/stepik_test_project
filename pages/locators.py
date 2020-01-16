from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    CARD_BUTTON = (By.CSS_SELECTOR, ".btn-group > a" )
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_FIELD = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_registration-password1")
    CONFIRM_PASSWORD = (By.CSS_SELECTOR,"#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "#register_form > .btn")

class ProductPageLocators():
    ADD_TO_CARD = (By.CLASS_NAME, "btn-add-to-basket")
    PRODUCT_NAME = (By.TAG_NAME, "h1")
    BOOK_NAME_ALERT = (By.CSS_SELECTOR, ".alertinner > strong")
    PRICE_BOOK = (By.CSS_SELECTOR, ".product_main > .price_color")
    PRICE_CARD_ALERT = (By.CSS_SELECTOR, ".alertinner > p > strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alertinner")

class BasketPageLocators():
    CARD_CONTENT = (By.CLASS_NAME, "basket-item")
    TEXT_EMPTY_CARD = (By.CSS_SELECTOR, "#content_inner > p")

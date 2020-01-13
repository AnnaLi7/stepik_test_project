from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_TO_CARD = (By.CLASS_NAME, "btn-add-to-basket")
    PRODUCT_NAME = (By.TAG_NAME, "h1")
    BOOK_NAME_ALERT = (By.CSS_SELECTOR, ".alertinner > strong")
    PRICE_BOOK = (By.CSS_SELECTOR, ".product_main > .price_color")
    PRICE_CARD_ALERT = (By.CSS_SELECTOR, ".alertinner > p > strong")

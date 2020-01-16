from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By

class ProductPage(BasePage):
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Success message is presented, but should not be"

    def should_not_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Success message is disappeared, but should not"

    def click_button_add_to_card(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_CARD)
        button.click()

    def should_be_product_name_in_message(self):
        prod_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME_ALERT).text
        assert prod_name == book_name, "Product name on page and in card are different"

    def should_be_same_price_of_card_and_product(self):
        prod_price = self.browser.find_element(*ProductPageLocators.PRICE_BOOK).text
        card_price = self.browser.find_element(*ProductPageLocators.PRICE_CARD_ALERT).text
        assert prod_price == card_price, "Product price on page and in card are different"

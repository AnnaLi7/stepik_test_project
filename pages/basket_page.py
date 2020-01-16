from .base_page import BasePage
from .locators import BasketPageLocators
from selenium.webdriver.common.by import By

class BasketPage(BasePage):
    def should_be_empty_card(self):
        assert self.is_not_element_present(*BasketPageLocators.CARD_CONTENT), "Card is not empty"

    def should_be_text_empty_card(self):
        text = self.browser.find_element(*BasketPageLocators.TEXT_EMPTY_CARD).text
        assert text == "Your basket is empty. Continue shopping", "Card is not empty"

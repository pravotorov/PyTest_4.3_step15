from .basePage import BasePage
from .locators import ProductPageLocators
from utils.error_messages import get_missing_element_error_message
from utils.waits import wait_until_element_is_clickable


class ProductPage(BasePage):
    def add_product_to_cart(self):
        add_to_cart_btn = wait_until_element_is_clickable(self.browser, ProductPageLocators.ADD_TO_CART_BUTTON)
        add_to_cart_btn.click()
        self.solve_quiz_and_get_code()

    def add_product_to_cart_without_quiz(self):
        add_to_cart_btn = wait_until_element_is_clickable(self.browser, ProductPageLocators.ADD_TO_CART_BUTTON)
        add_to_cart_btn.click()

    def should_be_correct_added_to_cart_success_message(self):
        self.should_be_added_to_cart_success_message()
        self.should_be_added_to_cart_success_message_with_correct_item_name()

    def should_be_added_to_cart_success_message(self):
        assert self.is_element_present(*ProductPageLocators.ADDED_SUCCESSFULLY_TO_CART_MESSAGE), (
            get_missing_element_error_message('Product added successfully message'))

    def should_be_added_to_cart_success_message_with_correct_item_name(self):
        added_to_cart_message = self.browser.find_element(*ProductPageLocators.ADDED_SUCCESSFULLY_TO_CART_MESSAGE).text
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        assert added_to_cart_message == product_name, (
            'Product name is incorrect in Product added successfully message')

    def should_be_correct_cart_total_message(self):
        self.should_be_cart_total_message()
        self.should_be_cart_total_message_with_correct_total_price()

    def should_be_cart_total_message(self):
        assert self.is_element_present(*ProductPageLocators.CART_TOTAL_MESSAGE), (
                get_missing_element_error_message('Total cart message'))

    def should_be_cart_total_message_with_correct_total_price(self):
        total_cart_message = self.browser.find_element(*ProductPageLocators.CART_TOTAL_MESSAGE).text
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        assert total_cart_message == product_price, (
            'Product price is incorrect in Total cart message')

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ADDED_SUCCESSFULLY_TO_CART_MESSAGE), (
            'Success message should not be shown, but is present on the page')

    def should_disappear_success_message(self):
        assert self.is_disappeared_element(*ProductPageLocators.ADDED_SUCCESSFULLY_TO_CART_MESSAGE), (
            'Success message should disappear, but is present on the page')

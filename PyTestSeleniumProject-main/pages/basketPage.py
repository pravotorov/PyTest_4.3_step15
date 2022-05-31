from pages.basePage import BasePage
from pages.locators import CartPageLocators


class BasketPage(BasePage):
    def should_be_empty(self):
        self.should_be_empty_cart_message()
        self.should_be_no_cart_items_form()

    def should_be_empty_cart_message(self):
        assert self.is_element_present(*CartPageLocators.EMPTY_CART_MESSAGE), (
            'No "Empty cart" message is shown on cart page')

    def should_be_no_cart_items_form(self):
        assert self.is_not_element_present(*CartPageLocators.CART_ITEMS_FORM), '"Cart items" form is shown on cart page'

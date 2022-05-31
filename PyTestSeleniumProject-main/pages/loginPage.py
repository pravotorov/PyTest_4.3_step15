import time

import pytest

from .basePage import BasePage
from .locators import LoginPageLocators
from utils.error_messages import get_missing_element_error_message
from utils.scroll_utils import scroll_element_into_view


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert '/login/' in self.browser.current_url, 'URL does not contain "/login/"'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), get_missing_element_error_message('Login form')

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), get_missing_element_error_message(
            'Register form')

    def register_new_user(self, email, password):
        register_email_field = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL_FIELD)
        register_password_field = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_FIELD)
        register_confirm_password_field = self.browser.find_element(*LoginPageLocators.REGISTER_CONFIRM_PASSWORD_FIELD)
        registration_submit_button = self.browser.find_element(*LoginPageLocators.REGISTER_SUBMIT_BUTTON)

        scroll_element_into_view(self.browser, register_email_field)
        register_email_field.send_keys(email)

        scroll_element_into_view(self.browser, register_password_field)
        register_password_field.send_keys(password)

        scroll_element_into_view(self.browser, register_confirm_password_field)
        register_confirm_password_field.send_keys(password)

        time.sleep(1)

        scroll_element_into_view(self.browser, registration_submit_button)
        registration_submit_button.click()

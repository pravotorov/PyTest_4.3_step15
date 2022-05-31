import math

from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from pages.locators import BasePageLocators
from utils.conf import TIMEOUT
from utils.waits import wait_until_element_is_clickable, wait_for_element_to_be_present


class BasePage:
    def __init__(self, browser, url, timeout=TIMEOUT):
        self.browser = browser
        self.url = url
        self.timeout = timeout

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, locator_type, locator):
        try:
            self.browser.find_element(locator_type, locator)
        except NoSuchElementException:
            return False

        return True

    def is_not_element_present(self, locator_type, locator, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(ec.presence_of_element_located((locator_type, locator)))
        except TimeoutException:
            return True

        return False

    def is_disappeared_element(self, locator_type, locator, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, poll_frequency=1, ignored_exceptions=TimeoutException
                          ).until_not(ec.presence_of_element_located((locator_type, locator)))
        except TimeoutException:
            return False

        return True

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def go_to_login_page(self):
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), 'Login link is missing'

    def select_view_cart_button(self):
        view_cart_button = wait_until_element_is_clickable(self.browser, BasePageLocators.VIEW_CART_BUTTON)
        view_cart_button.click()

    def should_be_authorised_user(self):
        assert wait_for_element_to_be_present(self.browser, BasePageLocators.USER_ICON), (
            'User icon is not shown, probably unauthorised user.')

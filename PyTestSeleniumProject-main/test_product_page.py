import time

import pytest

from pages.basketPage import BasketPage
from pages.loginPage import LoginPage
from pages.productPage import ProductPage
from pages.locators import ProductPageLocators


def test_guest_should_see_login_link_on_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.need_review
@pytest.mark.parametrize('promo', ["promo=offer0", "promo=offer1", "promo=offer2", "promo=offer3", "promo=offer4",
                                   "promo=offer5", "promo=offer6",
                                   pytest.param("promo=offer7", marks=pytest.mark.xfail),
                                   "promo=offer8", "promo=offer9"])
def test_guest_can_add_product_to_basket(browser, promo):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?{promo}"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_cart()
    page.should_be_correct_added_to_cart_success_message()
    page.should_be_correct_cart_total_message()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_cart()
    page.is_not_element_present(*ProductPageLocators.ADDED_SUCCESSFULLY_TO_CART_MESSAGE)


def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)
    page.open()
    page.is_not_element_present(*ProductPageLocators.ADDED_SUCCESSFULLY_TO_CART_MESSAGE)


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_cart()
    page.is_disappeared_element(*ProductPageLocators.ADDED_SUCCESSFULLY_TO_CART_MESSAGE)


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.select_view_cart_button()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty()


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'
        login_page = LoginPage(browser, link)
        login_page.open()
        email = str(time.time()) + 'test@yopmail.com'
        login_page.register_new_user(email=email, password='qwe456789')
        login_page.should_be_authorised_user()

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        page = ProductPage(browser, link)
        page.open()
        page.is_not_element_present(*ProductPageLocators.ADDED_SUCCESSFULLY_TO_CART_MESSAGE)

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?"
        page = ProductPage(browser, link)
        page.open()
        page.add_product_to_cart_without_quiz()
        page.should_be_correct_added_to_cart_success_message()
        page.should_be_correct_cart_total_message()

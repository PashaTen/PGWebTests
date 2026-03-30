import allure

from core.BaseTest import browser
from pages.BasePage import BasePage
from pages.LoginPage import LoginPageHelper

BASE_URL = 'https://ok.ru/'
EMPTY_LOGIN_ERROR = 'Введите логин'

@allure.suite('Проверка формы авторизации')
@allure.title('Проверка ошибки при пустой форме авторизации')
def test_empty_login_and_password(browser):
    BasePage(browser).get_url(BASE_URL)

    LoginPage = LoginPageHelper(browser)
    LoginPage.click_login()
    assert LoginPage.get_error_text() == EMPTY_LOGIN_ERROR


@allure.suite('Проверка форма авторизации')
@allure.title('Проверка формы авторизации без пароля')
def login_without_password(browser):
    BasePage(browser).get_url(BASE_URL)
    Login_page = LoginPageHelper(browser)
    Login_page.click_login()
    assert Login_page.get_error_text() == EMPTY_LOGIN_ERROR

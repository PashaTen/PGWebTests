import allure

from core.BaseTest import browser
from pages.BasePage import BasePageHelper
from pages.HelpPage import HelpPageHelper,HelpPageLocators
from pages.AdvertismentCabinetHelp import AdvertismentCabinetHelpPageHelper

BASE_URL = 'https://ok.ru/help'

@allure.suite('Проверка страницы Помощь')
@allure.title('Проверка скролла и перехода на страницу Рекламный кабинет')
def test_help_test(browser):
    BasePageHelper(browser).get_url(BASE_URL)
    HelpPage = HelpPageHelper(browser)
    HelpPage.scrollToitem(HelpPageLocators.ADVERTISMENT_CABINET)
    AdvertismentCabinetHelpPageHelper(browser)
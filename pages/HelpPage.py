from selenium.webdriver import ActionChains

from pages.BasePage import BasePageHelper
from selenium.webdriver.common.by import By
import allure

class HelpPageLocators:
    SEARCH_FIELD = (By.XPATH, '//input[@type="search"]')
    ACTUAL_TODAY = (By.XPATH,"//div//div[text()='Сегодня актуально']")
    REGISTRATION = (By.XPATH, "//div//div[text()='Регистрация']")
    MY_PROFILE = (By.XPATH, "//div//div[text()='Мой профиль']")
    COMMUNICATION = (By.XPATH, "//div//div[text()='Общение']")
    PROFILE_ACCESS = (By.XPATH, "//div//div[text()='Доступ к профилю']")
    SECURITY = (By.XPATH, "//div//div[text()='Безопасность']")
    GROUPS = (By.XPATH, "//div//div[text()='Группы']")
    PAYED_FUNCTION = (By.XPATH, "//div//div[text()='Платные функции']")
    SPAM = (By.XPATH, "//div//div[text()='Нарушения и спам']")
    GAMES_AND_APPS = (By.XPATH, "//div//div[text()='Игры и приложения']")
    OTHER_SERVICES = (By.XPATH, "//div//div[text()='Другие сервисы']")
    IMPORTANT_INFORMATION = (By.XPATH, "//div//div[text()='Полезная информация']")
    ADVERTISMENT_CABINET = (By.XPATH, "//div//div[text()='Рекламный кабинет']")

class HelpPageHelper(BasePageHelper):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    @allure.step('Проверяем загрузку страницы Помощи')
    def check_page(self):
        with allure.step('Проверяем корректность загрузки страницы'):
            self.attach_screenshot()
        self.find_element(HelpPageLocators.SEARCH_FIELD)
        self.find_element(HelpPageLocators.ACTUAL_TODAY)
        self.find_element(HelpPageLocators.REGISTRATION)
        self.find_element(HelpPageLocators.MY_PROFILE)
        self.find_element(HelpPageLocators.COMMUNICATION)
        self.find_element(HelpPageLocators.PROFILE_ACCESS)
        self.find_element(HelpPageLocators.SECURITY)
        self.find_element(HelpPageLocators.GROUPS)
        self.find_element(HelpPageLocators.PAYED_FUNCTION)
        self.find_element(HelpPageLocators.SPAM)
        self.find_element(HelpPageLocators.GAMES_AND_APPS)
        self.find_element(HelpPageLocators.OTHER_SERVICES)
        self.find_element(HelpPageLocators.IMPORTANT_INFORMATION)
        self.find_element(HelpPageLocators.ADVERTISMENT_CABINET)

    @allure.step('Проверяем скролл до нужного элемента')
    def scrollToitem(self,locator):
        scroll_item = self.find_element(locator)
        ActionChains(self.driver).scroll_to_element(scroll_item).click(scroll_item).perform()
import allure
from pages.BasePage import BasePage
from selenium.webdriver.common.by import By
import random

class RegistrationPageLocators:
    PHONE_FIELD = (By.XPATH, '//input[@placeholder="+7 000 000 00 00"]')
    COUNTRY_LIST = (By.CSS_SELECTOR, '.vkuiInput__host')
    COUNTRY_ITEM = (By.CSS_SELECTOR, '.vkuiInput__host')
    SUBMIT_BUTTON = (By.XPATH, '//*[@class="vkuiButton__content"]')

class RegistrationPageHelper(BasePage):
    def __init__(self, driver):
        self.driver = driver


    @allure.step('Проверяем загрузку страницы регистрации')
    def check_page(self):
        with allure.step("Проверяем корректность загрузки страницы"):
            self.find_element(RegistrationPageLocators.PHONE_FIELD)
            self.find_element(RegistrationPageLocators.COUNTRY_LIST)
            self.find_element(RegistrationPageLocators.SUBMIT_BUTTON)

    @allure.step('Выбираем случайную страну')
    def select_random_country(self):
        self.find_element(RegistrationPageLocators.COUNTRY_LIST).click()
        country_items = self.find_elements(RegistrationPageLocators.COUNTRY_ITEM)
        random_number = random.randint(0, 212)
        country_code = country_items[random_number].get_attribute('text')
        country_items[random_number].click()
        return country_code

    @allure.step('Получаем значение из поля телефона')
    def get_phone_field_value(self):
        return self.find_element(RegistrationPageLocators.PHONE_FIELD).get_attribute('value')
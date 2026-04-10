import allure
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait

from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_TAB = (By.XPATH, '//*[@data-l="t,login_tab"]')
    QR_TAB = (By.XPATH, '//*[@data-l="t,qr_tab"]')
    LOGIN_FIELD = (By.ID, 'field_email')
    PASSWORD_FIELD = (By.ID, 'field_password')
    LOGIN_BUTTON = (By.CSS_SELECTOR,
                    '.vkuiInternalTappable.vkuiButton__host.vkuiButton__sizeL.vkuiButton__modePrimary.vkuiButton__appearanceAccent.vkuiButton__sizeYNone.vkuiButton__stretched.vkuiTappable__host.vkuiTappable__sizeXNone.vkuiTappable__hasPointerNone.vkuiClickable__host.vkuiClickable__realClickable.vkuistyles__-focus-visible.vkuiRootComponent__host')
    LOGIN_BY_QR_CODE = (By.CSS_SELECTOR,
                        '.vkuiInternalTappable.vkuiButton__host.vkuiButton__sizeL.vkuiButton__modePrimary.vkuiButton__appearanceAccent.vkuiButton__sizeYNone.vkuiButton__stretched.vkuiTappable__host.vkuiTappable__sizeXNone.vkuiTappable__hasPointerNone.vkuiClickable__host.vkuiClickable__realClickable.vkuistyles__-focus-visible.vkuiRootComponent__host')
    RESTORE_LINK = (By.CSS_SELECTOR,
                    '.vkuiInternalTappable.vkuiLink__host.vkuiLink__withUnderline.vkuiTappable__host.vkuiTappable__sizeXNone.vkuiTappable__hasPointerNone.vkuiClickable__host.vkuiClickable__realClickable.vkuistyles__-focus-visible.vkuiRootComponent__host')
    REGISTRATION_BUTTON = (By.CSS_SELECTOR,
                           '.vkuiInternalTappable.vkuiButton__host.vkuiButton__sizeL.vkuiButton__modeSecondary.vkuiButton__appearanceNeutral.vkuiButton__sizeYNone.vkuiButton__stretched.vkuiTappable__host.vkuiTappable__sizeXNone.vkuiTappable__hasPointerNone.vkuiClickable__host.vkuiClickable__realClickable.vkuistyles__-focus-visible.vkuiRootComponent__host')
    VK_BUTTON = (By.CSS_SELECTOR, '.i.ic.social-icon.__s.__vk_id')
    MAIL_BUTTON = (By.CSS_SELECTOR, '.i.ic.social-icon.__s.__mailru')
    YANDEX_BUTTON = (By.CSS_SELECTOR, '.i.ic.social-icon.__s.__yandex')
    OTHER_BUTTON = (By.CSS_SELECTOR,
                    '.SeparatedText-module__root___B0ZfD.SeparatedText-module__line___CqNui.vkuiSubhead__host.vkuiSubhead__sizeYNone.vkuiTypography__host.vkuiTypography__normalize.vkuiRootComponent__host')
    ERROR_TEXT = (By.CSS_SELECTOR,
                  '.LoginForm-module__error___1xmAD.vkuiCaption__sizeYNone.vkuiCaption__level1.vkuiTypography__host.vkuiTypography__normalize.vkuiRootComponent__host')
    GO_BACK_BUTTON = (By.XPATH,
                      'class="vkuiInternalTappable vkuiButton__host vkuiButton__sizeL vkuiButton__modePrimary vkuiButton__appearanceAccent vkuiButton__sizeYNone vkuiButton__stretched vkuiTappable__host vkuiTappable__sizeXNone vkuiTappable__hasPointerNone vkuiClickable__host vkuiClickable__realClickable vkuistyles__-focus-visible vkuiRootComponent__host"')
    SUPPORT_BUTTON = (By.XPATH, '//*[@ class="support-link_items"]')


class LoginPageHelper(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        with allure.step('Проверяем корректность загрузки страницы'):
            self.attach_screenshot()
        self.find_element(LoginPageLocators.LOGIN_TAB)
        self.find_element(LoginPageLocators.QR_TAB)
        self.find_element(LoginPageLocators.LOGIN_FIELD)
        self.find_element(LoginPageLocators.PASSWORD_FIELD)
        self.find_element(LoginPageLocators.LOGIN_BUTTON)
        self.find_element(LoginPageLocators.LOGIN_BY_QR_CODE)
        self.find_element(LoginPageLocators.RESTORE_LINK)
        self.find_element(LoginPageLocators.REGISTRATION_BUTTON)
        self.find_element(LoginPageLocators.VK_BUTTON)
        self.find_element(LoginPageLocators.MAIL_BUTTON)
        self.find_element(LoginPageLocators.YANDEX_BUTTON)
        self.find_element(LoginPageLocators.OTHER_BUTTON)


    @allure.step('Нажимаем на кнопку "Войти"')
    def click_login(self):
        self.find_element(LoginPageLocators.LOGIN_BUTTON).click()
        self.attach_screenshot()

    @allure.step('Получаем текст ошибки')
    def get_error_text(self):
        self.attach_screenshot()
        return self.find_element(LoginPageLocators.ERROR_TEXT).text

    @allure.step('Заполняем поле логин')
    def type_login(self, login):
        self.find_element(LoginPageLocators.LOGIN_FIELD).send_keys(login)
        self.attach_screenshot()

    @allure.step('Заполняем поле пароль')
    def send_login_keys(self, password):
        self.find_element(LoginPageLocators.PASSWORD_FIELD).send_keys(password)
        self.attach_screenshot()

    @allure.step('Переходим к восстановлению')
    def click_recovery(self):
        self.find_element(LoginPageLocators.RESTORE_LINK).click()
        self.attach_screenshot()

    @allure.step('Переходим к регистрации')
    def click_registration(self):
        self.attach_screenshot()
        self.find_element(LoginPageLocators.REGISTRATION_BUTTON).click()

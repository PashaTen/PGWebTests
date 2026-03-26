from pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class LoginPageLocators:
    LOGIN_FIELD = (By.ID, 'field_email')
    LOGIN_BUTTON = (By.XPATH, '//*[@id="tabpanel-login-9186554079"]/vkid-form-adapter/div/div/div/div[1]/form/button/span')
    LOGIN_SHOW_HIDE_PASSWORD=(By.XPATH,'//*[@id="tabpanel-login-492477137"]/vkid-form-adapter/div/div/div/div[1]/form/div[2]/span/div/div[2]/span/button')
    LOGIN_UPPER_ENTRANCE=(By.XPATH, '//*[@id="login-9186554079"]')
    LOGIN_TOP_QR_ENTRANCE=(By.XPATH,'//*[@id="qrCode-9186554120"]')
    LOGIN_QR_BUTTON=(By.XPATH, '//*[@id="tabpanel-login-9186554079"]/vkid-form-adapter/div/div/div/div[1]/button/span')
    LOGIN_FORGOT_PASSWORD=(By.XPATH,'//*[@id="tabpanel-login-9186554079"]/vkid-form-adapter/div/div/div/div[1]/span/button')
    LOGIN_VK=(By.XPATH,'//*[@id="tabpanel-login-492477137"]/vkid-form-adapter/div/div/div/div[3]/div[4]/ui-part/div/a[1]/i')
    LOGIN_MAIL=(By.XPATH,'//*[@id="tabpanel-login-492477137"]/vkid-form-adapter/div/div/div/div[3]/div[4]/ui-part/div/a[2]/i')
    LOGIN_YANDEX=(By.XPATH,'//*[@id="tabpanel-login-492477137"]/vkid-form-adapter/div/div/div/div[3]/div[4]/ui-part/div/a[3]/i')



class LoginPageHelper(BasePage):
    pass
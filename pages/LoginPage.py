from pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class LoginPageLocators:
    LOGIN_FIELD = (By.ID, 'field_email')
    LOGIN_BUTTON = (By.ID, 'field_password')
    LOGIN_SHOW_HIDE_PASSWORD=(By.CLASS_NAME,'vkuiTappable__stateLayer vkuiTappable__ripple')
    LOGIN_UPPER_ENTRANCE=(By.XPATH, '//*[@data-l="t,login_tab"]')
    LOGIN_TOP_QR_ENTRANCE=(By.XPATH,'//*[@data-l="t,qr_tab"]')
    LOGIN_QR_BUTTON=(By.CLASS_NAME,'vkuiIcon vkuiIcon--24 vkuiIcon--w-24 vkuiIcon--h-24 vkuiIcon--qr_24')
    LOGIN_FORGOT_PASSWORD=(By.CLASS_NAME,'vkuiInternalTappable vkuiLink__host vkuiLink__withUnderline vkuiTappable__host vkuiTappable__sizeXNone vkuiTappable__hasPointerNone vkuiClickable__host vkuiClickable__realClickable vkuistyles__-focus-visible vkuiRootComponent__host')
    LOGIN_SIGN_UP=(By.CLASS_NAME,'vkuiInternalTappable vkuiButton__host vkuiButton__sizeL vkuiButton__modeSecondary vkuiButton__appearanceNeutral vkuiButton__sizeYNone vkuiButton__stretched vkuiTappable__host vkuiTappable__sizeXNone vkuiTappable__hasPointerNone vkuiClickable__host vkuiClickable__realClickable vkuistyles__-focus-visible vkuiRootComponent__host')
    LOGIN_VK=(By.CLASS_NAME, 'i ic social-icon __s __vk_id')
    LOGIN_MAIL=(By.CLASS_NAME,'i ic social-icon __s __mailru')
    LOGIN_YANDEX=(By.CLASS_NAME,'i ic social-icon __s __yandex')



class LoginPageHelper(BasePage):
    pass
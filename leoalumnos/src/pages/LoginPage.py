from leoalumnos.src.pages.locators.LoginPageLocators import LoginPageLocators
from leoalumnos.src.configs.configs import LOGIN_URL
from leoalumnos.src.SeleniumExtended import SeleniumExtended
from selenium.webdriver.common.by import By
import time

class LoginPage(LoginPageLocators):
    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def go_to_login_page(self):
        self.driver.get(LOGIN_URL)

    def input_code(self, code):
        self.sl.wait_and_send_keys(self.CODE_INPUT, code)
    
    def input_nip(self, nip):
        self.sl.wait_and_send_keys(self.NIP_INPUT, nip)
        
    def input_login_credentials(self, code, nip):
        self.input_code(code)
        self.input_nip(nip)
        time.sleep(5)
        self.click_login_btn()
    
    def click_login_btn(self):
        self.sl.wait_and_click(self.LOGIN_BTN)
        time.sleep(5)
from siiau.src.pages.locators.LoginPageLocators import LoginPageLocators
from siiau.src.configs.configs import LOGIN_URL
from siiau.src.SeleniumExtended import SeleniumExtended
from selenium.webdriver.common.by import By
import time

class LoginPage(LoginPageLocators):
    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def go_to_login_page(self):
        self.driver.get(LOGIN_URL)

    def input_code(self, code):
        # self.sl.wait_and_send_keys(self.CODE_INPUT, code)
        self.driver.find_element(By.CSS_SELECTOR, 'body > table > tbody > tr > td:nth-child(1) > table > tbody > tr:nth-child(1) > td > input[type=text]').click()
    
    def input_nip(self, nip):
        # self.sl.wait_and_send_keys(self.NIP_INPUT, nip)
        # self.driver.find_element(By.CSS_SELECTOR, 'input[name="p_clave_c"]').click()
        pass
        

    def input_login_credentials(self, code, nip):
        self.input_code(code)
        self.input_nip(nip)
        time.sleep(5)
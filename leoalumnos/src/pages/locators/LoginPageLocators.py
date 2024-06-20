from selenium.webdriver.common.by import By

class LoginPageLocators:
  CODE_INPUT = (By.ID, 'login-codigo')
  NIP_INPUT = (By.ID, 'login-password')
  LOGIN_BTN = (By.CSS_SELECTOR, 'button[type="submit"]')
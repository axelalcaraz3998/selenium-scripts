from selenium.webdriver.common.by import By

class LoginPageLocators:
  CODE_INPUT = (By.CSS_SELECTOR, 'input[name="p_codigo_c"]')
  NIP_INPUT = (By.CSS_SELECTOR, 'input[name="p_clave_c"]')
  CAPTCHA = (By.ID, 'recaptcha-anchor')
  LOGIN_BTN = (By.CSS_SELECTOR, 'button[type="submit"]')
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class SeleniumExtended:
  def __init__(self, driver):
    self.driver = driver
    self.default_wait = 10

  def wait_and_click(self, locator, timeout=None):
    timeout = timeout or self.default_wait
    WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator)).click()

  def wait_and_send_keys(self, locator, keys, timeout=None):
    timeout = timeout or self.default_wait
    WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator)).send_keys(keys)
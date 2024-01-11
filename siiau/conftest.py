from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
import siiau.config as config
import pytest

@pytest.fixture(scope="class")
def init_driver(request):
    supported_browsers = ["chrome", "firefox", "edge", "headlesschrome", "headlessfirefox", "headlessedge"]
    browser = config.BROWSER.lower()
    
    if not browser:
      raise Exception("The browser is not specified. Please specify the browser in the config.py file.")
    elif browser not in supported_browsers:
      raise Exception("The browser is not supported. Please specify a supported browser in the config.py file.")
    
    if browser == "chrome":
      driver = webdriver.Chrome()
    elif browser == "firefox":
      driver = webdriver.Firefox()
    elif browser == "edge":
      driver = webdriver.Edge()
    elif browser == "headlesschrome":
      options = ChromeOptions()
      options.add_argument("--headless")
      driver = webdriver.Chrome(options=options)
    elif browser == "headlessfirefox":
      options = FirefoxOptions()
      options.add_argument("--headless")
      driver = webdriver.Firefox(options=options)
    elif browser == "headlessedge":
      options = EdgeOptions()
      options.add_argument("--headless")
      driver = webdriver.Edge(options=options)

    request.cls.driver = driver
    yield
    driver.close()
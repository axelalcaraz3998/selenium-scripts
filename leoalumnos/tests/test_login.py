import pytest
from leoalumnos.src.pages.LoginPage import LoginPage
from leoalumnos.config import CODE, NIP

@pytest.mark.usefixtures("init_driver")
class TestLogin:
  @pytest.mark.test_login
  def test_login(self):
    login_page = LoginPage(self.driver)

    # Go to login page
    login_page.go_to_login_page()

    # Input login credentials
    login_page.input_login_credentials(CODE, NIP)


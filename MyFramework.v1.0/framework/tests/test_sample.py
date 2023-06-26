# tests/test_sample.py

import pytest
from framework.utils.driver import create_driver
from framework.config.settings import URL, USERNAME, PASSWORD
from framework.pages.login_page import LoginPage
from framework.pages.home_page import HomePage

@pytest.fixture(scope="module")
def driver():
    driver = create_driver()  # Create the web driver instance
    yield driver
    driver.quit()

def test_login(driver):
    driver.get(URL)

    login_page = LoginPage(driver)
    login_page.enter_credentials(USERNAME, PASSWORD)
    login_page.click_login_button()

    home_page = HomePage(driver)
    welcome_msg = home_page.get_welcome_message()
    assert "Logged In Successfully" in welcome_msg

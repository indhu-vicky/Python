# pages/login_page.py

from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_locator = (By.ID, "username")
        self.password_locator = (By.ID, "password")
        self.submit_btn_locator = (By.ID, "submit")

    def enter_credentials(self, username, password):
        self.driver.find_element(*self.username_locator).send_keys(username)
        self.driver.find_element(*self.password_locator).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*self.submit_btn_locator).click()

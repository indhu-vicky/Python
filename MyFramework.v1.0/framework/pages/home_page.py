# pages/home_page.py

from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.welcome_msg_locator = (By.CLASS_NAME, "post-title")

    def get_welcome_message(self):
        return self.driver.find_element(*self.welcome_msg_locator).text


##expecting message: Logged In Successfully
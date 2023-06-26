# utils/driver.py

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from framework.config.settings import BROWSER

def create_driver():
    if BROWSER == "chrome":
        options = ChromeOptions()
        # Add any desired Chrome options here
        driver = webdriver.Chrome(options=options)
    elif BROWSER == "firefox":
        options = FirefoxOptions()
        # Add any desired Firefox options here
        driver = webdriver.Firefox(options=options)
    else:
        raise ValueError("Invalid browser specified in settings")

    # Additional driver setup can be added here, such as timeouts or window size

    return driver

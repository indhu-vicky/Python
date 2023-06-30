from selenium import webdriver
import time
## Note: We didn't import pytest here

def test_setup():
    ##making driver as global variable
    global driver
    driver=webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()
    time.sleep(5)

def test_login():
    driver.find_element("xpath","//input[@placeholder='Username']").send_keys("Admin")
    driver.find_element("xpath","//input[@placeholder='Password']").send_keys("admin123")
    driver.find_element("xpath","//button[@type='submit']").click()
    x=driver.title
    ## Success scenario
    assert x == "OrangeHRM"
    ## Fail scenario
    ## assert x == "abc"
    time.sleep(5)

def test_teardown():
    driver.close()
    driver.quit()
    print("Sample Test Completed")
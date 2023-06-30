from selenium import webdriver
import time
import pytest

##setting fixtures
@pytest.fixture()
def test_setup():
    global driver
    driver=webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()
    time.sleep(5)
    ## things to do after test complete
    yield
    driver.close()
    driver.quit()
    print("Fixture Test Completed")

## giving fixture function as parameter here
def test_login(test_setup):
    driver.find_element("xpath","//input[@placeholder='Username']").send_keys("Admin")
    driver.find_element("xpath","//input[@placeholder='Password']").send_keys("admin123")
    driver.find_element("xpath","//button[@type='submit']").click()
    x=driver.title
    assert x == "OrangeHRM"
    time.sleep(5)
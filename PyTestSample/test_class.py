from selenium import webdriver
import time
import pytest

##setting class
class TestSample():
    @pytest.fixture()
    ##making it self
    def test_setup(self):
        global driver
        driver=webdriver.Chrome()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        driver.maximize_window()
        time.sleep(5)
        yield
        driver.close()
        driver.quit()
        print("Class Test Completed")
    
    ## passing self as parameter
    def test_login(self,test_setup):
        driver.find_element("xpath","//input[@placeholder='Username']").send_keys("Admin")
        driver.find_element("xpath","//input[@placeholder='Password']").send_keys("admin123")
        driver.find_element("xpath","//button[@type='submit']").click()
        x=driver.title
        assert x == "OrangeHRM"
        time.sleep(5)
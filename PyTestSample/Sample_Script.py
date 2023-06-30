from selenium import webdriver
import time

driver=webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
time.sleep(5)

driver.find_element("xpath","//input[@placeholder='Username']").send_keys("Admin")
driver.find_element("xpath","//input[@placeholder='Password']").send_keys("admin123")
driver.find_element("xpath","//button[@type='submit']").click()
time.sleep(5)

driver.close()
driver.quit()
print("Test Completed")


## This is a sample selenium script to login ##
## The same actions are used in different ways with PyTest ##
## PyTest have some issues in my local system, To execute any pytest follow below commands ##
## Open command prompt as system admin > use this command >>
## pytest {E:\path\filename.py} ##
## Notes for pytest ##
# $$every py filename should be test_*.py or *_test.py
# $$every function >> def test_*():
# $$every classname >> class Test*():

"""
Learn to click a button with Selenium

DISCLAIMER: This code is aimed at Selenium BEGINNERS
For more advanced tutorials and to learn how Qxf2 writes GUI automation, please visit our:
a) Our GUI automation guides: http://qxf2.com/gui-automation-diy
b) Other GitHub repos: https://github.com/qxf2

AUTHOR: Avinash Shetty
Contact: avinash@qxf2.com

SCOPE:
1) Launch Chrome driver
2) Navigate to wufoo
3) Find the Click me! button and click on it
4) Close the driver
"""
import time
from selenium import webdriver
def test_click():
    class button():
        def click_button(self):
# Create an instance of Chrome WebDriver
            self.driver = webdriver.Chrome()
# Maximize the browser window
            self.driver.maximize_window()
# Navigate to Qxf2 Tutorial page
            self.driver.get("https://secure.wufoo.com/signup/17/register/")

# KEY POINT: Locate the button and click on it
            button  = self.driver.find_element("xpath", "//input[@id='saveForm']")
            button.click()

# Pause the script to wait for page elements to load
            time.sleep(3)
# Close the browser
            self.driver.close()
    class facade():
        def __init__(self):
            self.action=button()
        def start_test(self):
            self.action.driver


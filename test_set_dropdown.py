"""
Learn to set dropdowns with Selenium

DISCLAIMER: This code is aimed at Selenium BEGINNERS
For more advanced tutorials and to learn how Qxf2 writes GUI automation, please visit our:
a) Our GUI automation guides: http://qxf2.com/gui-automation-diy
b) Other GitHub repos: https://github.com/qxf2

AUTHOR: Avinash Shetty
Contact: avinash@qxf2.com

SCOPE:
1) Launch Chrome Driver
2) Navigate to spotify page
3) Set Month to july in the dropdown
4) Close the browser
"""
import time
from selenium import webdriver
def test_dropdown():
    class dropdown():
        def select(self):
# Create an instance of Firefox WebDriver
            self.driver = webdriver.Chrome()
# Maximize the browser window
            self.driver.maximize_window()

# Navigate to Qxf2 Tutorial page
            self.driver.get("http://qxf2.com/selenium-tutorial-main")

# KEY POINT: Identify the dropdown and click on it
            dropdown_element = self.driver.find_element("xpath", "//button[@data-toggle='dropdown']")
            dropdown_element.click()
# Sleep is one way to pause while the page elements load
            time.sleep(1)

# KEY POINT: Locate a particular option and click on it
            self.driver.find_element("xpath", "//a[text()='Male']").click()
# Future tutorials cover explicit, implicit and ajax waits
            time.sleep(3)

# Close the browser window
            self.driver.close()
    # Close the browser
            self.driver.close()
    class facade():
        def __init__(self):
            self.action=dropdown()
        def check(self):
            self.action.driver
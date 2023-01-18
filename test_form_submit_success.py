"""
Learn to fill and submit a form with Selenium
DISCLAIMER: This code is aimed at Selenium BEGINNERS
For more advanced tutorials and to learn how Qxf2 writes GUI automation, please visit our:
a) Our GUI automation guides: http://qxf2.com/gui-automation-diy
b) Other GitHub repos: https://github.com/qxf2
AUTHOR: Avinash Shetty
Contact: avinash@qxf2.com
SCOPE:
1) Launch Chrome driver
2) Navigate to Qxf2 Tutorial page
3) Fill all the text field in Example form
4) Click on Click me! button
5) Verify user is taken to Selenium Tutorial redirect page
6) Close the browser
"""

import time
from selenium import webdriver
def test_form_submit():
    class form_submit():
        def submit_succes(self):

# Create an instance of CHrome WebDriver
            self.driver = webdriver.Chrome("E:/chromedriver.exe")
# Maximize the browser window
            self.driver.maximize_window()
# Navigate to Qxf2 Tutorial page
            self.driver.get("http://qxf2.com/selenium-tutorial-main")

#KEY POINT: Code to fill forms
# Find the name field and fill name
            name = self.driver.find_element("xpath", "//input[@id='name']")
            name.send_keys('Avinash')
# Find the email field and fill your email
            self.driver.find_element("xpath", "//input[@name='email']").send_keys('avinash@qxf2.com')
# Find the phone no field and fill phone no
            phone = self.driver.find_element("id", "phone")
            phone.send_keys('9999999999')
# Identify the xpath for Click me button and click on it
            button = self.driver.find_element("xpath", "//button[text()='Click me!']")
            button.click()
# Wait for the new page to load
            time.sleep(3)
# Verify user is taken to Qxf2 tutorial redirect url
            if self.driver.current_url== 'https://qxf2.com/selenium-tutorial-redirect':
                print("Success")
            else:
                print("Failure")

# Close the browser
            self.driver.close()
    class facade():
        def __init__(self):
            self.action=form_submit()
        def check(self):
            self.action.driver

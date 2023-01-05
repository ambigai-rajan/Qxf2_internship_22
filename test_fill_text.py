"""
Learn to fill text fields with Selenium

DISCLAIMER: This code is aimed at Selenium BEGINNERS
For more advanced tutorials and to learn how Qxf2 writes GUI automation, please visit our:
a) Our GUI automation guides: http://qxf2.com/gui-automation-diy
b) Other GitHub repos: https://github.com/qxf2

AUTHOR: Avinash Shetty
Contact: avinash@qxf2.com

SCOPE:
1) Launch Chrome Driver
2) Navigate to woofo webpage
3) Find elements using id, xpath, xpath without id
4) Fill name, email and phone no in the respective fields
5) Close the browser
"""
import time
from selenium import webdriver

# Create an instance of Firefox WebDriver
driver = webdriver.Chrome("e:/chromedriver.exe")

# KEY POINT: The driver.get method will navigate to a page given by the URL
driver.get('https://secure.wufoo.com/signup/17/register/')

# Check if the title of the page is proper
if driver.title=="Wufoo!":
    print ("Success: Wufoo!")
else:
    print ("Failed: Wufoo!")
# Find the email field using xpath with id
name = driver.find_element("xpath", "//input[@id='email']")
# KEY POINT: Send text to an element using send_keys method
name.send_keys('dummy245677@gmail.com')

# Find the password field using xpath without id
email = driver.find_element("xpath", "//input[@id='password']")
email.send_keys('123456789')

# Find the phone no field using xpath
phone = driver.find_element("xpath", "//input[@id='wufooName']")
phone.send_keys('woofuuu')

# Sleep is one way to wait for things to load
# Future tutorials cover explicit, implicit and ajax waits
time.sleep(3)

# Close the browser window
driver.close()

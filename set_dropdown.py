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

# Create an instance of Firefox WebDriver
driver = webdriver.Chrome("E:/chromedriver.exe")
# Maximize the browser window
driver.maximize_window()

# Navigate to Qxf2 Tutorial page
driver.get("https://www.spotify.com/in-en/signup?forward_url=https%3A%2F%2Fopen.spotify.com%2F")

# KEY POINT: Identify the dropdown and click on it
dropdown_element = driver.find_element("xpath", "//select[@id='month']")
dropdown_element.click()
# Sleep is one way to pause while the page elements load
time.sleep(4)

# KEY POINT: Locate a particular option and click on it
driver.find_element("xpath", "//option[@value='07']").click()
# Future tutorials cover explicit, implicit and ajax waits
time.sleep(3)

# Close the browser window
driver.close()

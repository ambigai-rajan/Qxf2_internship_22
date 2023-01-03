"""
Learn to select a checkbox using Selenium

DISCLAIMER: This code is aimed at Selenium BEGINNERS
For more advanced tutorials and to learn how Qxf2 writes GUI automation, please visit our:
a) Our GUI automation guides: http://qxf2.com/gui-automation-diy
b) Other GitHub repos: https://github.com/qxf2

AUTHOR: Avinash Shetty
Contact: avinash@qxf2.com

SCOPE:
1) Launch Chrome Driver
2) Navigate to spotify
3) Find the Checkbox element in the Example form and enable it
4) Close the browser
"""
import time
from selenium import webdriver
def test_checkbox():
# Create an instance of Firefox WebDriver
    driver = webdriver.Chrome()
# Maximize the browser window
    driver.maximize_window()
    driver.get("https://www.spotify.com/in-en/signup?forward_url=https%3A%2F%2Fopen.spotify.com%2F")
# KEY POINT:to close the popup
    
    driver.find_element("xpath","//button[@class='onetrust-close-btn-handler onetrust-close-btn-ui banner-close-button ot-close-icon']").click()

# KEY POINT: Locate the checkbox and click on it
    checkbox = driver.find_element("xpath", "//span[@class='Indicator-sc-1airx73-0 ihUlHW']")
    checkbox.click()

# Pause the script for 3 sec so you can confirm the check box was selected
    time.sleep(3)

# Close the browser window
    driver.close()

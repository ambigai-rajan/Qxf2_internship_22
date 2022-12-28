"""
Learn to navigate to a URL using Selenium

DISCLAIMER: This code is aimed at Selenium BEGINNERS
For more advanced tutorials and to learn how Qxf2 writes GUI automation, please visit our:
a) Our GUI automation guides: http://qxf2.com/gui-automation-diy
b) Other GitHub repos: https://github.com/qxf2

AUTHOR: Avinash Shetty
Contact: avinash@qxf2.com

SCOPE:
1) Launch Chrome Driver
2) Navigate to woofu webpage
3) Check the page title
4) Close the browser
"""
from selenium import webdriver

# Create an instance of Firefox WebDriver
browser = webdriver.Chrome("e:chromedriver.exe")

# KEY POINT: The driver.get method will navigate to a page given by the URL
browser.get('https://secure.wufoo.com/signup/17/register/')

# Check if the title of the page is proper
if browser.title == "Wufoo!":

    print ("Success: Wufoo!")
else:
    print ("Failed: Wufoo!")

# Quit the browser window
browser.quit()

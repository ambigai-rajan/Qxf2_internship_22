"""
Learn to hover over elements using Selenium

DISCLAIMER: This code is aimed at Selenium BEGINNERS
For more advanced tutorials and to learn how Qxf2 writes GUI automation, please visit our:
a) Our GUI automation guides: http://qxf2.com/gui-automation-diy
b) Other GitHub repos: https://github.com/qxf2

AUTHOR: Avinash Shetty
Contact: avinash@qxf2.com

SCOPE:
1) Launch Chrome driver
2) Navigate to Qxf2 HICAS page
3) Click on Menu icon
4) Hover over Resource and GUI automation and click on GUI automation link
5) Close the browser
"""

import time
from selenium import webdriver

#Notice this extra import statement!
from selenium.webdriver.common.action_chains import ActionChains
def test_hover():
    class hover():
        def check_hover(self):
# Create an instance of Firefox WebDriver
            self.driver = webdriver.Chrome("e:/chromedriver.exe")
# Maximize the browser window
            self.driver.maximize_window()
# Navigate to Qxf2 Tutorial page
            self.driver.get("https://www.hicas.ac.in/")

# Locate the Menu icon and click on it
            menu = self.driver.find_element("xpath", "//div[@class='menuIcon']")
            menu.click()

# Locate the Resource element to hover over
            resource = self.driver.find_element("xpath", "//a[@href='news-events']")
            resource.click()

# KEY POINT: Use ActionChains to hover over elements
            action = ActionChains(self.driver)
            action.perform()
            time.sleep(2) #Adding waits to make the example more visual


# Wait for 3 seconds for the page to load
            time.sleep(3)

# Close the browser
            self.driver.close()
    # Close the browser
            self.driver.close()
    class facade():
        def __init__(self):
            self.action=hover()
        def check(self):
            self.action.driver

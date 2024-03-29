"""
Learn to count the rows in a table using Selenium

DISCLAIMER: This code is aimed at Selenium BEGINNERS
For more advanced tutorials and to learn how Qxf2 writes GUI automation, please visit our:
a) Our GUI automation guides: http://qxf2.com/gui-automation-diy
b) Other GitHub repos: https://github.com/qxf2

AUTHOR: Avinash Shetty
Contact: avinash@qxf2.com

SCOPE:
1) Launch Firefox driver
2) Navigate to Qxf2 Tutorial page
3) Find the no of rows in the Example tabel
4) Close the browser
"""
import time
from selenium import webdriver
def test_count_rows():
    class count_rows():
        def count(self):
# Create an instance of Firefox WebDriver
            self.driver = webdriver.Chrome("E:/chromedriver.exe")
# Maximize the browser window
            self.driver.maximize_window()
# Navigate to Qxf2 Tutorial page
            self.driver.get("https://www.google.com/search?q=fifa+points+table&oq=fifa+points+&aqs=chrome.0.0i433i512j69i57j0i512l8.10310j1j15&sourceid=chrome&ie=UTF-8#sie=lg;/m/0fp_8fm;2;/m/030q7;st;fp;1;;;")

# Find the table element in the page
            table = self.driver.find_element("xpath", "//div[@jsname='LS81yb']")

# KEY POINT: Find the tr elements in the table
            rows = table.find_elements("xpath", "//tbody/descendant::tr")
            print(f"Total No of Rows: {len(rows)}")

# Pause the script for 3 seconds
            time.sleep(3)

# Close the browser
            self.driver.close()
    class facade():
        def __init__(self):
            self.action=count_rows()
        def check(self):
            self.action.driver
"""
Learn to parse the text within each cell of a table

DISCLAIMER: This code is aimed at Selenium BEGINNERS
For more advanced tutorials and to learn how Qxf2 writes GUI automation, please visit our:
a) Our GUI automation guides: http://qxf2.com/gui-automation-diy
b) Other GitHub repos: https://github.com/qxf2

AUTHOR: Avinash Shetty
Contact: avinash@qxf2.com

SCOPE:
1) Launch Firefox driver
2) Navigate to Qxf2 Tutorial page
3) Get all the fields from the table
4) Close the browser
"""
import time
from selenium import webdriver
def test_table():
# Create an instance of WebDriver
    driver = webdriver.Chrome()
# Maximize the browser window
    driver.maximize_window()
# Navigate to Qxf2 Tutorial page
    driver.get("https://www.google.com/search?q=fifa+points+table&oq=fifa+points+&aqs=chrome.0.0i433i512j69i57j0i512l8.10310j1j15&sourceid=chrome&ie=UTF-8#sie=lg;/m/0fp_8fm;2;/m/030q7;st;fp;1;;;")

# KEY POINT: Logic to get the text in each cell of the table
# Find the Example table element in the page
    table = driver.find_element("xpath","//div[@jsname='LS81yb']")
# Use find_elements_by_xpath method to get the rows in the table
    rows = table.find_elements("xpath","//tbody/descendant::tr")
# Create a list to store the text
    result_data = []
# Go to each row and get the no of columns and the navigate to column
# Then get the text from each column
    for i, row in enumerate(rows):
    # Find no of columns by getting the td elements in each row
        cols = row.find_elements("tag_name","td")
        cols_data = []
        for j, col in enumerate(cols):
        # Get the text of each field
            cols_data.append(col.text.encode('utf-8'))
        result_data.append(cols_data)

# Print the result list
    print(result_data)

# Pause the script for 3 sec
    time.sleep(3)
    

# Close the browser
    driver.close()

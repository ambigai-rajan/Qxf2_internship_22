import time
from selenium import webdriver
a=webdriver.Chrome("E:/chromedriver.exe")
a.get("https://www.craiyon.com/")
a.find_element("xpath","//div[@id='prompt']").send_keys("child in mars")
a.find_element("xpath","//button[@type='button']").click()
time.sleep(10)
a.quit()
"""module explain test the craiyon.com """
import time
from selenium import webdriver
driver=webdriver.Chrome("E:/chromedriver.exe")
driver.get("https://www.craiyon.com/")
driver.find_element("xpath","//div[@id='prompt']").send_keys("child in mars")
driver.find_element("xpath","//button[@type='button']").click()
time.sleep(120)

driver.quit()

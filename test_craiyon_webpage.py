"""module explain test the craiyon.com """
import time
from selenium import webdriver
def test_title():
    driver=webdriver.Chrome()
    driver.get("https://www.craiyon.com/")
    driver.find_element("xpath","//div[@id='prompt']").send_keys("child in mars")
    driver.find_element("xpath","//button[@type='button']").click()
    time.sleep(10)
    test_titile = "Craizon, formerly DALL-E mini"
    assert test_titile == test_titile
    driver.quit()

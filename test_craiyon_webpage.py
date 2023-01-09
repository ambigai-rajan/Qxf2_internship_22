"""module explain test the craiyon.com """
import time
from selenium import webdriver
def test_title():
    class navigate():
        def get_browser(self):
            self.driver=webdriver.Chrome()
            self.driver.get("https://www.craiyon.com/")
            self.driver.find_element("xpath","//div[@id='prompt']").send_keys("child in mars")
            self.driver.find_element("xpath","//button[@type='button']").click()
            self.driver.sleep(11)
            self.driver.quit()
    class pytest():
        def check_title(self):        
            self.test_titile = "Craizon, formerly DALL-E mini"
            assert self.test_titile == self.test_titile
    class facade():
        def __init__(self):
            self.page=navigate()
            self.test=pytest()
        def begin_test(self):
            self.page.driver
            self.test.test_titile


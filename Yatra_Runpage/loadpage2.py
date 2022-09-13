from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
import time
class All():
    def test_all(self):
        driver = webdriver.Chrome("/\\Drivers\\chromedriver.exe")
        print('Browser launch success.')
        driver.maximize_window()
        driver.get('https://www.yatra.com/')
        print('Test URL open success.')
        time.sleep(2)

obj = All()
obj.test_all()
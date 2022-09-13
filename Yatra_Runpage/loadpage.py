from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
import time
class Yatrapageload():
    def pageload(self):
        driver = webdriver.Chrome("/\\Drivers\\chromedriver.exe")
        print('Browser launch success.')
        driver.maximize_window()
        yatra = 'https://www.yatra.com/'
        driver.get(yatra)
        print('Test URL open success.')
        time.sleep(2)

obj = Yatrapageload()
obj.pageload()
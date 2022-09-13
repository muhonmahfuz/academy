from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select

class Button():
    def test_button(self):
        executable_path= 'I:\\Software Testing\\python\\rcvacademy\\Drivers\\chromedriver.exe'
        driver = webdriver.Chrome(executable_path)
        print('Browser launch success.')
        driver.maximize_window()
        driver.get("https://www.yatra.com/")
        print('Test URL open success.')

        # Scroll page

        driver.execute_script("window.scrollTo(500,910)")
        print("scrolled")
        time.sleep(5)


testObj = Button()
testObj.test_button()
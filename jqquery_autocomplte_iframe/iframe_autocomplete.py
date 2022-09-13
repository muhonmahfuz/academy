from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select

class Button():
    def test_button(self):
        executable_path = "I:\\Software Testing\\python\\rcvacademy\\Drivers\\chromedriver.exe"
        driver = webdriver.Chrome(executable_path)
        print('Browser launch success.')
        driver.maximize_window()
        driver.get("https://jqueryui.com/autocomplete")
        print('Test URL open success.')

        # SELECT A SPEED
        #driver.find_element(By.XPATH, "//iframe[@class='demo-frame']")
        driver.switch_to.frame(0)
        print("switch to iframe")
        time.sleep(2)

        # driver.find_element(By.XPATH, "//body")
        # print("called div body, second frame, this frame contain speed,file,number,title")

        # driver.find_element(By.XPATH, "//div[@class='ui-widget']")
        # print("after called div now clicked in select a speed button")
        # time.sleep(2)

        # driver.find_element(By.XPATH, "//input[@id='tags']").click()
        # time.sleep(3)

        typetag = driver.find_element(By.XPATH, "//input[@id='tags']")
        typetag.click()
        time.sleep(2)
        typetag.send_keys("MUHON")
        time.sleep(2)



testObj = Button()
testObj.test_button()
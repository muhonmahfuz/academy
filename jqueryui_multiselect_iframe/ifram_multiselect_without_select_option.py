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
        driver.get("https://jqueryui.com/selectable")
        print('Test URL open success.')


        driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@class='demo-frame']"))
        print("switch to iframe")
        time.sleep(2)




        driver.find_element(By.XPATH,"//li[normalize-space()='Item 1']").click()
        print("item 4")
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[normalize-space()='Item 1']").click()
        print("item 4")
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[normalize-space()='Item 2']").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[normalize-space()='Item 3']").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[normalize-space()='Item 4']").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[normalize-space()='Item 5']").click()
        time.sleep(1)




testObj = Button()
testObj.test_button()
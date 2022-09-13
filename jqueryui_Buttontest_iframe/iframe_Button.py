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
        driver.get("https://jqueryui.com/button")
        print('Test URL open success.')



        driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@class='demo-frame']"))
        print("switch to iframe")
        time.sleep(2)




        # driver.find_element(By.XPATH, "(//a[@role='button'])[1]").click()
        # print("Widget Buttons=An Anchor button")
        # time.sleep(2)
        #
        driver.find_element(By.XPATH, "//button[@class='ui-button ui-corner-all ui-widget']").click()
        print("Widget Buttons=An button element")
        time.sleep(2)
        #
        # driver.find_element(By.XPATH, "(//input[@role='button'])[1]").click()
        # print("Widget Buttons=A submit button")
        # time.sleep(2)
        #
        # driver.find_element(By.XPATH,"//button[@class='ui-button ui-widget ui-corner-all']").click()
        # print("CSS Button= A Button element")
        # time.sleep(2)
        #
        driver.find_element(By.XPATH, "(//input[@class='ui-button ui-widget ui-corner-all'])[1]").click()
        print("CSS Button= A submit element")
        time.sleep(2)
        #
        driver.find_element(By.XPATH, "(//input[@class='ui-button ui-widget ui-corner-all'])[1]").click()
        print("CSS Button= A Anchor element")
        time.sleep(2)


testObj = Button()
testObj.test_button()
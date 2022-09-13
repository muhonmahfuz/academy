from selenium import webdriver
from selenium.webdriver import ActionChains
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
        driver.get("https://jqueryui.com/droppable/")
        print('Test URL open success.')

        driver.switch_to.frame(0)
        print("switch to iframe")
        time.sleep(2)

        firstelmt=driver.find_element(By.XPATH,"//div[@id='draggable']")
        secondelmt=driver.find_element(By.XPATH,"//div[@id='droppable']")

        actions=ActionChains(driver)

        actions.drag_and_drop(firstelmt,secondelmt).perform()
        print("perform actions")
        time.sleep(3)

        # SECOND WAY ACTION

        # driver.switch_to.frame(0)
        # print("switch to iframe")
        # time.sleep(2)
        #
        # ActionChains(driver).drag_and_drop(driver.find_element(By.XPATH,"//div[@id='draggable']"),driver.find_element(By.XPATH,"//div[@id='droppable']")).perform()
        # time.sleep(3)



testObj = Button()
testObj.test_button()
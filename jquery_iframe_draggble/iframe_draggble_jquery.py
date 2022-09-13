import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class All():
    def test_all(self):
        executable_path = "I:\\Software Testing\\python\\rcvacademy\\Drivers\\chromedriver.exe"
        driver = webdriver.Chrome(executable_path)
        print('Browser launch success.')
        driver.maximize_window()
        driver.get("https://jqueryui.com/draggable/")
        print('Test URL open success.')

        #first page scroll

        #Using click and hold

        driver.execute_script("window.scrollTo(0,340)")
        time.sleep(3)

        driver.switch_to.frame(0)
        print("switched to frame")


        droppable=driver.find_element(By.XPATH, "//div[@id='draggable']")
        actions=ActionChains(driver)

        #Using click and hold
        actions.click_and_hold(droppable).perform()
        time.sleep(2)
        # Using drag_and_drop_by_offset
        actions.drag_and_drop_by_offset(droppable,200,400).perform()
        time.sleep(2)
        driver.execute_script("window.scrollTo(0,200)")
        time.sleep(2)








testObj = All()
testObj.test_all()
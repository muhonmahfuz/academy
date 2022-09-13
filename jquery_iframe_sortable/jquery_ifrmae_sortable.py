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
        driver.get("https://jqueryui.com/sortable/")
        print('Test URL open success.')

        # first page scroll

        driver.execute_script("window.scrollTo(0,300)")
        time.sleep(3)

        driver.switch_to.frame(0)
        print("switched to frame")

        item1 = driver.find_element(By.XPATH, "//li[normalize-space()='Item 1']")
        item2 = driver.find_element(By.XPATH, "//li[normalize-space()='Item 2']")
        item3 = driver.find_element(By.XPATH, "//li[normalize-space()='Item 3']")
        item4 = driver.find_element(By.XPATH, "//li[normalize-space()='Item 4']")
        item5 = driver.find_element(By.XPATH, "//li[normalize-space()='Item 5']")
        item6 = driver.find_element(By.XPATH, "//li[normalize-space()='Item 6']")
        item7 = driver.find_element(By.XPATH, "//li[normalize-space()='Item 7']")

        actions=ActionChains(driver)

        actions.click_and_hold(item7).perform()
        time.sleep(1)
        actions.drag_and_drop_by_offset(item7,0,-131).perform()
        time.sleep(3)

        actions.click_and_hold(item1).perform()
        time.sleep(1)
        actions.drag_and_drop_by_offset(item1,0,220).perform()
        time.sleep(3)

        actions.click_and_hold(item2).perform()
        time.sleep(1)
        actions.drag_and_drop_by_offset(item2,0,140).perform()
        time.sleep(3)

        actions.click_and_hold(item5).perform()
        time.sleep(2)
        actions.drag_and_drop_by_offset(item5,0,-100).perform()
        time.sleep(5)

        actions.click_and_hold(item6).perform()
        time.sleep(2)
        actions.drag_and_drop_by_offset(item6,0,-150).perform()
        time.sleep(3)

        actions.click_and_hold(item1).perform()
        time.sleep(2)
        actions.drag_and_drop_by_offset(item1,0,-109).perform()
        time.sleep(3)

        actions.click_and_hold(item4).perform()
        time.sleep(2)
        actions.drag_and_drop_by_offset(item4,0,188).perform()
        time.sleep(3)

        # actions.click_and_hold(item1).perform()
        # time.sleep(2)
        # actions.release(item6).perform()
        # time.sleep(5)
        #
        # actions.drag_and_drop(item1,item5).perform()
        # time.sleep(5)
        # actions.drag_and_drop(item2,item6).perform()
        # time.sleep(2)
        # actions.drag_and_drop(item3, item7).perform()
        # time.sleep(2)
        # actions.drag_and_drop(item7, item5).perform()
        # time.sleep(2)

        #// span[ @class ='ui-slider-handle ui-corner-all ui-state-default ui-state-focus ui-state-hover']
        #// *[@ id="slider"] / span
        #// span[@ class ='ui-slider-handle ui-corner-all ui-state-default']



testObj = All()
testObj.test_all()
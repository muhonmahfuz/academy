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
        driver.get("https://jqueryui.com/slider/")
        print('Test URL open success.')

        # first page scroll

        driver.execute_script("window.scrollTo(0,300)")
        time.sleep(3)

        driver.switch_to.frame(0)
        print("switched to frame")

        slider_button=driver.find_element(By.XPATH, "//*[@id='slider']/span")
        actions=ActionChains(driver)
        actions.click_and_hold(slider_button).perform()
        time.sleep(2)
        actions.drag_and_drop_by_offset(slider_button,340,15).perform()
        time.sleep(2)

        #// span[ @class ='ui-slider-handle ui-corner-all ui-state-default ui-state-focus ui-state-hover']
        #// *[@ id="slider"] / span
        #// span[@ class ='ui-slider-handle ui-corner-all ui-state-default']



testObj = All()
testObj.test_all()
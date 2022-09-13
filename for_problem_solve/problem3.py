# main work
# driver.switch_to.new_window  (its result open a new window and than next write a line given below)
# (store as variable) parent/child01/child02 = driver.current_window_handle (this commond result this opened new window now can handle posible)
# then you call url  driver.get("http://www.google.com")
# by those step you do more window open and handle all of it
# একটি web/url থেকে new window open হয় তাহলে এইভাবে window handle করা যাবে না

import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Keys, ActionChains
# from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
import pytest

class Test_multi_window_pytest:
    @pytest.fixture(scope="session")
    def setUp(self):
        global driver
        executable_path = "I:\\Software Testing\\python\\rcvacademy\\Drivers\\chromedriver.exe"
        driver = webdriver.Chrome(executable_path)
        driver.implicitly_wait(75)
        print('Browser launch success.')
        driver.maximize_window()

        yield
        driver.quit()


    # @pytest.mark.skip
    def test_new_window_handle_01(self,setUp):
        global driver
        driver.get("https://www.google.com")
        parent_window=driver.current_window_handle
        driver.execute_script("window.open('http://www.yatra.com','new window')")
        time.sleep(3)
        all_child = driver.window_handles
        for child02 in all_child:
            if child02 != parent_window:
                driver.switch_to.window(child02)
                # driver.find_element(By.XPATH, "//a[normalize-space()='View All']")
                # time.sleep(3)
        driver.switch_to.window(parent_window)
        time.sleep(1)
        driver.execute_script("window.open('http://www.facebook.com','new window')")
        all_child=driver.window_handles
        for child01 in all_child:
            if child01 != parent_window:
                driver.switch_to.window(child01)
                time.sleep(4)




        driver.switch_to.window(parent_window)
        time.sleep(1)
        driver.execute_script("window.open('http://www.being.com','new window')")
        all_child = driver.window_handles
        for child03 in all_child:
            if child03 != parent_window:
                driver.switch_to.window(child03)

        driver.switch_to.window(parent_window)
        time.sleep(1)
        driver.execute_script("window.open('http://www.gamil.com','new window')")
        all_child = driver.window_handles
        for child04 in all_child:
            if child04 != parent_window:
                driver.switch_to.window(child04)

        driver.switch_to.window(parent_window)
        time.sleep(1)
        driver.execute_script("window.open('http://www.apple.com','new window')")
        all_child = driver.window_handles
        for child05 in all_child:
            if child05 != parent_window:
                driver.switch_to.window(child05)

        driver.switch_to.window(parent_window)
        time.sleep(2)
        driver.switch_to.window(child01)
        time.sleep(2)
        driver.switch_to.window(child02)
        time.sleep(2)
        driver.switch_to.window(child03)
        time.sleep(2)
        driver.switch_to.window(parent_window)
        time.sleep(2)
        driver.switch_to.window(child05)
        time.sleep(2)
        driver.switch_to.window(child04)
        time.sleep(2)

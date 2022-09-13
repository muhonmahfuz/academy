#  যে window তে break দেয়া হবে সেই window আর handle করা যাবে না বাকিগুলা handle করা যাবে
#  একটি web/url থেকে new window open হয় তাহলে এইভাবে window handle করতে হয়

import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Keys, ActionChains
# from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
import pytest
class Test_youtube_pytest:
    @pytest.fixture(scope="session")
    def setUp(self):
        global driver
        # option = Options()
        # option.headless = True
        # executable_path = "I:\\Software Testing\\python\\rcvacademy\\Drivers\\chromedriver.exe"
        driver = webdriver.Chrome(executable_path = "I:\\Software Testing\\python\\rcvacademy\\Drivers\\chromedriver.exe")
        driver.implicitly_wait(15)
        print('Browser launch success.')
        driver.maximize_window()


        yield
        driver.quit()

    def test_new_window_handle_01(self, setUp):
        global driver
        driver.get("https://www.yatra.com/")
        print('Test URL open success.')

        parent_window = driver.current_window_handle
        print('hh1')
        all_child = driver.window_handles
        viewall1 = driver.find_element(By.XPATH, "//a[normalize-space()='View All']")
        viewall1.click()
        time.sleep(2)
        print('hh2')
        all_child = driver.window_handles
        for child02 in all_child:
            if child02 != parent_window:
                driver.switch_to.window(child02)
                # driver.find_element(By.XPATH, "//a[normalize-space()='View All']")
        #         # time.sleep(3)
        driver.switch_to.window(parent_window)
        time.sleep(1)
        driver.execute_script("window.open('http://www.facebook.com','new window')")
        all_child = driver.window_handles
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

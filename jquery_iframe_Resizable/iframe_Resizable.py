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
        driver.get("https://jqueryui.com/resizable/")
        print('Test URL open success.')

        # Scroll page 1.execute_script

        # driver.execute_script("window.scrollTo(0,309)")
        # print("scrolled")
        # time.sleep(3)

        # Scroll_to_element

        elmt2 = driver.find_element(By.XPATH, "//a[normalize-space()='Menu']")
        ations = ActionChains(driver)
        ations.scroll_to_element(elmt2).perform()
        print("scrolled")
        time.sleep(3)

        # Switch to frame

        driver.switch_to.frame(0)
        print("switch to iframe")

        elmt = driver.find_element(By.XPATH,
                                   "//div[@class='ui-resizable-handle ui-resizable-se ui-icon ui-icon-gripsmall-diagonal-se']")
        ations.drag_and_drop_by_offset(elmt, 350, 140).perform()
        print("test done")
        time.sleep(5)







testObj = Button()
testObj.test_button()
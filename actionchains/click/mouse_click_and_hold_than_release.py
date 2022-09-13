import time
from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
# from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
import pytest
class Test_youtube_pytest:
    @pytest.fixture(scope="session")
    def setUp(self):
        global driver
        executable_path = "I:\\Software Testing\\python\\rcvacademy\\Drivers\\chromedriver.exe"
        driver = webdriver.Chrome(executable_path)
        driver.implicitly_wait(15)
        print('Browser launch success.')
        driver.maximize_window()


        yield
        driver.quit()
    def test_mouse_click_and_hold_than_release(self,setUp):
        driver.get("https://jqueryui.com/selectable/")
        driver.execute_script("window.scrollTo(0,160)")
        driver.switch_to.frame(0)
        actions=ActionChains(driver)
        item1=driver.find_element(By.XPATH, "//li[normalize-space()='Item 1']")
        item2=driver.find_element(By.XPATH, "//li[normalize-space()='Item 2']")
        item3=driver.find_element(By.XPATH, "//li[normalize-space()='Item 3']")
        item4=driver.find_element(By.XPATH, "//li[normalize-space()='Item 4']")
        item5=driver.find_element(By.XPATH, "//li[normalize-space()='Item 5']")
        item6=driver.find_element(By.XPATH, "//li[normalize-space()='Item 6']")
        item7=driver.find_element(By.XPATH, "//li[normalize-space()='Item 7']")

        # actions.click_and_hold(item3).move_to_element(item6).perform()  # use move_to_element
        actions.click_and_hold(item3).release(item6).perform()  # use release

        time.sleep(3)
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
        options=Options()
        options.headless=True
        # executable_path = "I:\\Software Testing\\python\\rcvacademy\\Drivers\\chromedriver.exe"
        driver = webdriver.Chrome(options=options,executable_path = "I:\\Software Testing\\python\\rcvacademy\\Drivers\\chromedriver.exe")
        driver.implicitly_wait(15)
        print('Browser launch success.')
        driver.maximize_window()


        yield
        driver.quit()

    # @pytest.mark.skip
    def test_fb_login_valid_data(self,setUp):
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
        # actions.key_down(Keys.CONTROL).click(item1).perform()
        # actions.key_down(Keys.CONTROL).click(item2).perform()
        # actions.key_down(Keys.CONTROL).click(item3).perform()
        # actions.key_down(Keys.CONTROL).click(item4).perform()
        # actions.key_down(Keys.CONTROL).click(item5).perform()
        # actions.key_down(Keys.CONTROL).click(item6).perform()
        # actions.key_down(Keys.CONTROL).click(item7).perform()
        # actions.key_down(Keys.CONTROL).click(item4).perform()
        # time.sleep(2)
        # actions.key_down(Keys.CONTROL).click(item3).perform()
        # time.sleep(2)
        # actions.key_down(Keys.CONTROL).click(item2).perform()
        # time.sleep(2)
        # actions.key_down(Keys.CONTROL).click(item3).perform()
        # time.sleep(2)
        # actions.key_down(Keys.CONTROL).click(item2).perform()
        # time.sleep(2)
        # actions.key_down(Keys.CONTROL).click(item4).perform()
        actions.key_down(Keys.CONTROL).click(item1).key_down(Keys.CONTROL).click(item5).perform()
        time.sleep(2)


# # For Headless browser this work only
# from selenium.webdriver.chrome.options import Options
# class Test_youtube1_pytest:
#     def setUp(self):
#         global driver
#         options = Options()
#         options.headless = True
#         # executable_path = "I:\\Software Testing\\python\\rcvacademy\\Drivers\\chromedriver.exe"
#         driver = webdriver.Chrome(options=options,executable_path="I:\\Software Testing\\python\\rcvacademy\\Drivers\\chromedriver.exe")
#
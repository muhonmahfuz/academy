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


    # @pytest.mark.skip
    def test_select_all_key_down(self,setUp):
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
        actions.key_down(Keys.CONTROL).click(item1).perform()  # key_down এর মানে control button কে চেপে রাখছে যতক্কনা key_up করা হইছে  control button চাপাই থাকবে আবার key_down দিয়ে আরেকটা key চাপ দিলে যেমন shift তাইলে আগের সিলেক্ট ছুটে যাবে
        actions.click(item2).perform()
        actions.click(item3).perform()
        actions.click(item4).click(item5).click(item6).click(item7).click(item2).click(item3).click(item4).perform()
        # actions.key_down(Keys.CONTROL).click(item2).perform()
        # actions.key_down(Keys.CONTROL).click(item3).perform()
        # actions.key_down(Keys.CONTROL).click(item4).perform()
        # actions.key_down(Keys.CONTROL).click(item5).perform()
        # actions.key_down(Keys.CONTROL).click(item6).perform()
        # actions.key_down(Keys.CONTROL).click(item7).perform()
        # actions.key_down(Keys.CONTROL).click(item4).perform()
        # time.sleep(1)
        # actions.key_down(Keys.CONTROL).click(item3).perform()
        # time.sleep(1)
        # actions.key_down(Keys.CONTROL).click(item2).perform()
        # time.sleep(1)
        # actions.key_down(Keys.CONTROL).click(item3).perform()
        # time.sleep(1)
        # actions.key_down(Keys.CONTROL).click(item2).perform()
        # time.sleep(1)
        # actions.key_down(Keys.CONTROL).click(item4).perform()
        #
        # time.sleep(2)


    def test_select_key_up_in_middle_on_key_down(self,setUp):
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
        actions.key_down(Keys.CONTROL).click(item1).perform()
        actions.key_down(Keys.CONTROL).click(item2).perform()
        actions.key_down(Keys.CONTROL).click(item3).perform()
        actions.key_up(Keys.CONTROL).click(item4).perform()
        actions.key_down(Keys.CONTROL).click(item5).perform()
        actions.key_down(Keys.CONTROL).click(item6).perform()
        actions.key_up(Keys.CONTROL).click(item7).perform()
        actions.key_down(Keys.CONTROL).click(item4).perform()
        time.sleep(1)
        actions.key_down(Keys.CONTROL).click(item3).perform()
        time.sleep(1)
        actions.key_up(Keys.CONTROL).click(item2).perform()
        time.sleep(1)
        actions.key_down(Keys.CONTROL).click(item3).perform()
        time.sleep(1)
        actions.key_down(Keys.CONTROL).click(item2).perform()
        time.sleep(1)
        actions.key_down(Keys.CONTROL).click(item4).perform()

        time.sleep(2)








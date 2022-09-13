from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select

class All():
    def test_all(self):
        executable_path = "I:\\Software Testing\\python\\rcvacademy\\Drivers\\chromedriver.exe"
        driver = webdriver.Chrome(executable_path)
        print('Browser launch success.')
        driver.maximize_window()
        driver.get("https://jqueryui.com/checkboxradio")
        print('Test URL open success.')

        # SELECT LOCATION RADIOBOX

        driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@class='demo-frame']"))
        print("switch to iframe")
        time.sleep(2)

        driver.find_element(By.XPATH, "//div[@class='widget']")
        print("called div body, second frame, this frame contain speed,file,number,title")

        driver.find_element(By.XPATH, "//label[normalize-space()='Paris']").click()
        print("after called div now clicked in paris")
        time.sleep(2)

        driver.find_element(By.XPATH, "//label[normalize-space()='London']").click()
        print("after called div now clicked in london")
        time.sleep(2)

        driver.find_element(By.XPATH, "//label[normalize-space()='New York']").click()
        print("after called div now clicked in New York")
        time.sleep(2)

        # HOTEL RATINGS

        # driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@class='demo-frame']"))
        # print("switch to iframe")
        # time.sleep(2)
        #
        # driver.find_element(By.XPATH, "//div[@class='widget']")
        # print("called div body, second frame, this frame contain speed,file,number,title")
        #
        # driver.find_element(By.XPATH, "//label[normalize-space()='2 Star']").click()
        # print("after called div now clicked in 2 Star")
        # time.sleep(2)
        #
        # driver.find_element(By.XPATH, "//label[normalize-space()='3 Star']").click()
        # print("after called div now clicked in 3 Star")
        # time.sleep(2)
        #
        # driver.find_element(By.XPATH, "//label[normalize-space()='4 Star']").click()
        # print("after called div now clicked in 4 Star")
        # time.sleep(2)
        #
        # driver.find_element(By.XPATH, "//label[normalize-space()='2 Star']").click()
        # print("after called div now clicked in 2 Star")
        # time.sleep(2)
        #
        # driver.find_element(By.XPATH, "//label[normalize-space()='4 Star']").click()
        # print("after called div now clicked in 4 Star")
        # time.sleep(2)

        # BED TYPES

        # driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@class='demo-frame']"))
        # print("switch to iframe")
        # time.sleep(2)
        #
        # driver.find_element(By.XPATH, "//div[@class='widget']")
        # print("called div body, second frame, this frame contain speed,file,number,title")
        #
        # driver.find_element(By.XPATH, "//label[normalize-space()='2 Double']").click()
        # print("after called div now clicked in 2 Double")
        # time.sleep(2)
        #
        # driver.find_element(By.XPATH, "//label[normalize-space()='2 Queen']").click()
        # print("after called div now clicked in 2 Queen")
        # time.sleep(2)
        #
        # driver.find_element(By.XPATH, "//label[normalize-space()='1 King']").click()
        # print("after called div now clicked in 1 King")
        # time.sleep(2)
        #
        # driver.find_element(By.XPATH, "//label[normalize-space()='2 Queen']").click()
        # print("after called div now clicked in 2 Queen")
        # time.sleep(2)
        #
        # driver.find_element(By.XPATH, "//label[normalize-space()='2 Double']").click()
        # print("after called div now clicked in 2 Double")
        # time.sleep(2)


testObj = All()
testObj.test_all()
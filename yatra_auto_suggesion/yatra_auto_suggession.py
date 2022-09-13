from selenium import webdriver
import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class All():
    def test_all(self):
        executable_path = 'I:\\Software Testing\\python\\rcvacademy\\Drivers\\chromedriver.exe'
        driver = webdriver.Chrome(executable_path)
        print('Browser launch success.')
        driver.maximize_window()
        driver.get('https://www.yatra.com/')
        print('Test URL open success.')
        depart_from=driver.find_element(By.XPATH,"//input[@id='BE_flight_origin_city']")
        # depart_from.click()
        time.sleep(1)
        depart_from.clear()
        time.sleep(1)
        depart_from.send_keys("New")
        time.sleep(1)
        depart_from.send_keys(Keys.ENTER)
        time.sleep(1)
        going_to=driver.find_element(By.XPATH,"//input[@id='BE_flight_arrival_city']")
        going_to.click()
        going_to.send_keys("New")
        time.sleep(1)
        # driver.find_element
        #**** driver.find_elements
        search_results = driver.find_elements(By.XPATH,"//div[@class='viewport']//div[1]/li")
        # second way
        # driver.find_element(By.XPATH, "//div[@class='viewport']//div[1]/li[4]").click()
        # driver.find_element(By.CSS_SELECTOR, "div[class='oneway-roundtrip CitySwap'] li:nth-child(4)").click()
        # time.sleep(5)
        # time.sleep(3)
        print(len(search_results))
        for results in search_results:
            if "New York (JFK)" in results.text:
                results.click()
                time.sleep(3)
                break




testObj = All()
testObj.test_all()



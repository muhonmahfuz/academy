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
        depart_from.click()
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
        print(len(search_results))
        for results in search_results:
            if "New York (JFK)" in results.text:
                results.click()
                time.sleep(1)
                break


        # Calender use

        find_date_calender=driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_date']")
        find_date_calender.click()
        time.sleep(2)
        # driver.find_element(By.XPATH, "//div[@id='monthWrapper']")
        driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(2) > div:nth-child(1) > section:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > section:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > ul:nth-child(1) > li:nth-child(2) > ul:nth-child(1) > li:nth-child(1) > section:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3) > td:nth-child(7)").click()
        time.sleep(3)
        # all_dates=driver.find_elements(By.XPATH, "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']")
        # print(len(all_dates))
        # for date in all_dates:
        #     if date.get_attribute("date-date") == "20/08/2022":
        #         date.click()
        #         time.sleep(8)
        #         print("done")
        #         break



testObj = All()
testObj.test_all()



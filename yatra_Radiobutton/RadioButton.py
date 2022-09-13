from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
import time
class Radiobutton():
    def test_radiobutton(self):
        executable_path = "I:\\Software Testing\\python\\rcvacademy\\Drivers\\chromedriver.exe"
        driver = webdriver.Chrome(executable_path)
        print('Browser launch success.')
        driver.maximize_window()
        yatra = 'https://www.yatra.com/'
        driver.get(yatra)
        print('Test URL open success.')
        time.sleep(2)

        multicity=driver.find_element(By.XPATH, "//a[@title='Multicity']")
        multicity.click()
        print("click on Multicity")
        time.sleep(2)

        traveller=driver.find_element(By.XPATH, "//span[normalize-space()='Traveller']")
        traveller.click()
        print("click on Traveller")
        time.sleep(2)

        business=driver.find_element(By.XPATH, "//span[normalize-space()='Business']")
        business.click()
        print("click on Business")
        time.sleep(2)

        economy=driver.find_element(By.XPATH, "//span[normalize-space()='Economy']")
        economy.click()
        print("select Economy")
        time.sleep(2)

        premium_economy=driver.find_element(By.XPATH, "//span[normalize-space()='Premium Economy']")
        premium_economy.click()
        print("click on premium_economy")
        time.sleep(2)

        non_stop_flights=driver.find_element(By.XPATH, "//a[@title='Non Stop Flights']")
        non_stop_flights.click()
        print("click on non_stop_flights")
        time.sleep(2)

        non_stop_flights.click()
        print("click on non stop flight for deselect")
        time.sleep(2)



obj = Radiobutton()
obj.test_radiobutton()
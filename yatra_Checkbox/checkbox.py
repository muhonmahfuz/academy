from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
import time
class Checkbox():
    def test_checkbox(self):
        driver = webdriver.Chrome("I:\\Software Testing\\python\\rcvacademy\\Drivers\\chromedriver.exe")
        print('Browser launch success.')
        driver.maximize_window()
        driver.get('https://www.yatra.com/')
        print('the title is :'+driver.title)
        print('Test URL open success.')
        time.sleep(2)

        driver.find_element(By.XPATH, "//a[@title='Non Stop Flights']").click()
        time.sleep(2)
        print("select non stop flights")
        driver.find_element(By.XPATH, "//a[@title='Non Stop Flights']").click()
        time.sleep(2)
        print("deselect non stop flights")
        driver.find_element(By.XPATH, "//a[@title='Student Fare Offer']").click()
        time.sleep(2)
        print("select student fare")
        driver.find_element(By.XPATH, "//a[@title='Student Fare Offer']").click()
        time.sleep(2)
        print("deselect student fare")
        driver.find_element(By.XPATH, "//a[@title='Armed Forces Offer']").click()
        time.sleep(2)
        print("select armed forches")
        driver.find_element(By.XPATH, "//a[@title='Armed Forces Offer']").click()
        time.sleep(2)
        print("deselect armed forches")
        driver.find_element(By.XPATH, "//a[@title='Senior Citizen Offer']").click()
        time.sleep(2)
        print("select senior citizense")
        driver.find_element(By.XPATH, "//a[@title='Senior Citizen Offer']").click()
        time.sleep(2)
        print("deselect senior citizense")



obj = Checkbox()
obj.test_checkbox()
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
import time
class Yatrapageload():
    def pageload(self):
        driver = webdriver.Chrome("/\\Drivers\\chromedriver.exe")
        print('Browser launch success.')
        driver.maximize_window()
        yatra = 'https://www.yatra.com/'
        driver.get(yatra)
        print('Test URL open success.')
        time.sleep(2)

        driver.find_element(By.XPATH,"//span[normalize-space()='Hotels']").click()
        print('move to the Hotel option')
        time.sleep(1)

        driver.find_element(By.XPATH,"//input[@id='BE_hotel_htsearch_btn']").click()
        print('clicked on search and lounch book hotel page')
        time.sleep(1)

        driver.get(yatra)
        print("again lounch main yatra page")
        time.sleep(1)


        # Bus select

        driver.find_element(By.XPATH,"//span[normalize-space()='Buses']").click()
        print("clicked Bus option")
        time.sleep(1)
        driver.find_element(By.XPATH,"//input[@id='BE_bus_search_btn']").click()
        print("clicked search button")
        time.sleep(3)
        driver.find_element(By.XPATH, "//div[3]//div[1]//div[6]//button[1]//div[1]").click()
        print("select first option on busses list")
        time.sleep(2)







        driver.close()

obj = Yatrapageload()
obj.pageload()
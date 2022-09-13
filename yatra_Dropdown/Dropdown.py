from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
class Yatrapageload():
    def pageload(self):
        driver = webdriver.Chrome("I:\\Software Testing\\python\\rcvacademy\\Drivers\\chromedriver.exe")
        print('Browser launch success.')
        driver.maximize_window()
        yatra = 'https://www.yatra.com/'
        driver.get(yatra)
        print('Test URL open success.')
        time.sleep(2)

        driver.find_element(By.XPATH, "//span[normalize-space()='Holidays']").click()
        print("clicked holiday option")
        time.sleep(2)

        monthoftravel=driver.find_element(By.XPATH, "//div[@class='ddTitle borderRadiusTp holi_passengerBox']")

        monthoftravel.click()
        time.sleep(2)

        # driver.find_element(By.XPATH, "//div[@class='overview']")
        # print("called all option frame_ div overview")
        # time.sleep(2)
        #
        # monthoftravel_options=Select(monthoftravel)
        # monthoftravel_options.select_by_index("1")
        # print("clicked month of travel optional")
        # time.sleep(2)

        driver.find_element(By.XPATH, "//div[@class='overview']")
        print("called all option frame_ div overview")
        time.sleep(2)

        # driver.find_element(By.XPATH,"//span[normalize-space()='November 2022']").click()
        # print("than clicked on option from all option frame 'November 2022'")
        # time.sleep(3)
        # driver.find_element(By.XPATH, "//div[@class='smooth-banner-transition']//li[4]").click()
        # print("than clicked on option from all option frame 'September 2022'")
        # time.sleep(3)

        # driver.find_element(By.XPATH,"//div[@class='smooth-banner-transition']//li[7]").click()
        # print("than clicked on option from all option frame 'December 2022'")
        # time.sleep(3)

        driver.find_element(By.XPATH, "//span[normalize-space()='October 2022']").click()
        print("than clicked on option from all option frame 'October 2022'")
        time.sleep(3)

        # driver.find_element(By.XPATH, "//div[@class='select-with-bg holi_passengerBox flexB100']//li[2]").click()
        # print("than clicked on option from all option frame 'July 2022'")
        # time.sleep(3)

        # driver.find_element(By.XPATH, "//span[normalize-space()='August 2022']").click()
        # print("than clicked on option from all option frame 'August 2022'")
        # time.sleep(3)



obj = Yatrapageload()
obj.pageload()
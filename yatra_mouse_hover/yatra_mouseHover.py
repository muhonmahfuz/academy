from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select

class Button():
    def test_button(self):
        executable_path = "I:\\Software Testing\\python\\rcvacademy\\Drivers\\geckodriver.exe"
        driver = webdriver.Firefox(executable_path)
        print('Browser launch success.')
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get("https://www.yatra.com/")
        print('Test URL open success.')


        # More option

        moreoption = driver.find_element(By.XPATH, "//span[@class='more-arr']")

        actions = ActionChains(driver)
        actions.move_to_element(moreoption).perform()


        trains = driver.find_element(By.XPATH, "//span[normalize-space()='Trains']")
        trains.click()


        driver.execute_script("")

        alert = driver.find_element(By.XPATH, "//button[normalize-space()='OK']")

        alert.click()
        print("done")


        # LOGIN

        # dd = driver.find_element(By.XPATH, "//a[contains(text(),'My Account')]")
        # ActionChains(driver).move_to_element(dd).perform()
        # time.sleep(1)

        # loging=driver.find_element(By.XPATH,"//a[@id='signInBtn']")
        # loging.click()
        # time.sleep(2)
        #
        # input=driver.find_element(By.XPATH,"//input[@id='login-input']")
        # input.click()
        # input.send_keys("00112244")
        # time.sleep(3)
        # print("Done")

        # Sign up

        # dd = driver.find_element(By.XPATH, "//a[contains(text(),'My Account')]")
        # ActionChains(driver).move_to_element(dd).perform()
        # time.sleep(1)
        #
        # signup=driver.find_element(By.XPATH, "//a[@id='SignUpBtn']")
        # signup.click()
        # time.sleep(2)
        #
        # input = driver.find_element(By.XPATH, "//input[@id='login-input']")
        # input.click()
        # input.send_keys("00000000000")
        # time.sleep(3)




testObj = Button()
testObj.test_button()
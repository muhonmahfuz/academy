import time
from selenium import webdriver
from selenium.webdriver import Keys
# from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By


class All():
    def test_all(self):
        executable_path = 'I:\\Software Testing\\python\\rcvacademy\\Drivers\\chromedriver.exe'
        driver = webdriver.Chrome(executable_path)
        print('Browser launch success.')
        driver.maximize_window()
        driver.get('https://www.yatra.com/')
        print('Test URL open success.')

        dd = driver.find_element(By.XPATH, "//span[normalize-space()='Buses']")
        # # dd.screenshot("..\\test.png")
        dd.click()

        driver.save_screenshot("I:\\Software Testing\\python\\rcvacademy\\Screenshot\\error1.png")

        # driver.save_screenshot(".\\test1.png")
        driver.find_element(By.XPATH, "//span[normalize-space()='Hotels']").click()
        time.sleep(1)

        driver.save_screenshot("I:\\Software Testing\\python\\rcvacademy\\Screenshot\\error2.png")
        driver.close()


testObj = All()
testObj.test_all()

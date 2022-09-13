import time
from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
# from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By


class All():
    def test_all(self):
        executable_path = 'I:\\Software Testing\\python\\rcvacademy\\Drivers\\chromedriver.exe'
        driver = webdriver.Chrome(executable_path)
        print('Browser launch success.')
        driver.maximize_window()
        driver.get('https://demo.guru99.com/test/simple_context_menu.html')
        print('Test URL open success.')

        actions = ActionChains(driver)
        # right_click
        # right_click_path = driver.find_element(By.XPATH, "//span[@class='context-menu-one btn btn-neutral']")
        # actions.context_click(right_click_path).perform()
        # time.sleep(1)
        # double_click
        double_click_path = driver.find_element(By.XPATH, "//button[normalize-space()='Double-Click Me To See Alert']")
        actions.double_click(double_click_path).perform()
        time.sleep(1)
        driver.close()







testObj = All()
testObj.test_all()

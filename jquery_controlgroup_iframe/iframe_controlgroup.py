from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select

class Button():
    def test_button(self):
        executable_path = "I:\\Software Testing\\python\\rcvacademy\\Drivers\\chromedriver.exe"
        driver = webdriver.Chrome(executable_path)
        print('Browser launch success.')
        driver.maximize_window()
        driver.get("https://jqueryui.com/controlgroup")
        print('Test URL open success.')

        # SELECT A SPEED

        # iframe = driver.find_element(By.XPATH, "//iframe[@class='demo-frame']")
        driver.switch_to.frame(0)
        print("switch to iframe")
        time.sleep(2)

        # driver.find_element(By.XPATH, "//div[@class='widget']")
        # print("called div body, second frame, this frame contain speed,file,number,title")
        #
        # driver.find_element(By.XPATH, "//div[@class='controlgroup ui-controlgroup ui-controlgroup-horizontal ui-helper-clearfix']").click()
        # print("after called div now clicked in select a speed button")
        # time.sleep(2)

        # compact = driver.find_element(By.XPATH, "//span[@id='car-type-button']")
        # luxury = driver.find_element(By.XPATH, "//div[@class='ui-selectmenu-menu ui-front ui-selectmenu-open']//li[5]")
        standard = driver.find_element(By.XPATH,"//label[@for='transmission-standard']")
        insurance = driver.find_element(By.XPATH, "//label[@for='insurance']")

        driver.find_element(By.XPATH, "//span[@id='car-type-button']").click()
        print("after clicked speed button now call div class frame select-menu-open ")
        time.sleep(3)

        driver.find_element(By.XPATH, "//div[@class='ui-selectmenu-menu ui-front ui-selectmenu-open']//li[5]").click()
        print("after calling div class frame select-menu-open then call another frame div speed-menu")
        print("then you click on options of luxury")
        time.sleep(3)

        standard.click()
        print("option is standard")
        time.sleep(2)

        insurance.click()
        print("option is insurance")
        time.sleep(2)

        driver.find_element(By.XPATH, "//div[@class='controlgroup ui-controlgroup ui-controlgroup-horizontal ui-helper-clearfix']//span[@class='ui-button-icon ui-icon ui-icon-triangle-1-n']").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//div[@class='controlgroup ui-controlgroup ui-controlgroup-horizontal ui-helper-clearfix']//span[@class='ui-button-icon ui-icon ui-icon-triangle-1-n']").click()
        time.sleep(2)

        driver.find_element(By.XPATH,
                            "//div[@class='controlgroup ui-controlgroup ui-controlgroup-horizontal ui-helper-clearfix']//span[@class='ui-button-icon ui-icon ui-icon-triangle-1-n']").click()
        time.sleep(2)

        driver.find_element(By.XPATH,
                            "//div[@class='controlgroup ui-controlgroup ui-controlgroup-horizontal ui-helper-clearfix']//span[@class='ui-button-icon ui-icon ui-icon-triangle-1-s']").click()
        time.sleep(2)

        driver.find_element(By.XPATH,
                            "//div[@class='controlgroup ui-controlgroup ui-controlgroup-horizontal ui-helper-clearfix']//span[@class='ui-button-icon ui-icon ui-icon-triangle-1-s']").click()
        time.sleep(2)


        driver.find_element(By.XPATH, "//button[@class='ui-widget ui-controlgroup-item ui-button ui-corner-right']").click()
        print("option is Book now")
        time.sleep(2)


testObj = Button()
testObj.test_button()
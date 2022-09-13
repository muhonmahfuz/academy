from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select

class Button():
    def test_button(self):
        executable_path = "I:\\Software Testing\\python\\rcvacademy\\Drivers\\chromedriver.exe"
        driver = webdriver.Chrome(executable_path)
        driver.implicitly_wait(10)
        print('Browser launch success.')
        driver.maximize_window()
        driver.get("https://jqueryui.com/selectmenu")
        print('Test URL open success.')

        # scrolling

        # driver.execute_script("window.scrollTo(0,360)")
        # print("scrolled")
        # time.sleep(5)

        actions = ActionChains(driver)
        elm = driver.find_element(By.XPATH, "//a[normalize-space()='Selectmenu']")
        actions.scroll_to_element(elm).perform()
        # time.sleep(5)

        # SELECT A SPEED

        driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@class='demo-frame']"))
        print("switch to iframe")
        # time.sleep(2)
        #
        driver.find_element(By.XPATH, "//div[@class='demo']")
        print("called div body, second frame, this frame contain speed,file,number,title")

        driver.find_element(By.XPATH, "//span[@id='speed-button']").click()
        print("after called div now clicked in select a speed button")
        # time.sleep(2)
        #
        # driver.find_element(By.XPATH, "//div[@class='ui-selectmenu-menu ui-front ui-selectmenu-open']")
        # print("after clicked speed button now call div class frame select-menu-open ")
        #
        # driver.find_element(By.XPATH, "//ul[@id='speed-menu']")
        # print("after calling div class frame select-menu-open then call another frame div speed-menu")
        # print("then you click on options of speed-menu")
        #
        driver.find_element(By.XPATH,"//div[@id='ui-id-5']").click()
        print("option is Faster")
        # time.sleep(2)
        #
        # driver.find_element(By.XPATH, "//div[@id='ui-id-1']").click()
        # print("option is slower")
        # time.sleep(2)

        # SELECT A FILE

        # iframe_xpath=driver.find_element(By.XPATH,"//iframe[@class='demo-frame']")
        # driver.switch_to.frame(0)
        # print("switch to iframe")
        # time.sleep(2)

        # driver.find_element(By.XPATH, "//div[@class='demo']")
        # print("called div body, second frame, this frame contain speed,file,number,title")

        driver.find_element(By.XPATH,"//span[@id='files-button']").click()
        print("after called div now clicked in select a file")
        # time.sleep(2)
        #
        # driver.find_element(By.XPATH, "//div[@class='ui-selectmenu-menu ui-front ui-selectmenu-open']")
        # print("after clicked select file now call div class frame select-menu-open ")
        #
        # driver.find_element(By.XPATH, "//ul[@id='files-menu']")
        # print("after calling div class frame select-menu-open then call another frame div files-menu")
        # print("then you click on options of file-menu")
        # time.sleep(3)
        #
        #
        #
        driver.find_element(By.XPATH,"//div[@class='ui-selectmenu-menu ui-front ui-selectmenu-open']//li[3]").click()
        print("option is li[3] = ui.jQuery.js")
        # time.sleep(2)
        #
        # # driver.find_element(By.XPATH, "//div[@class='ui-selectmenu-menu ui-front ui-selectmenu-open']//li[6]").click()
        # # print("option is li[6] = some other file with a very long text")
        # # time.sleep(2)



        # SELECT NUMBER

        # driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@class='demo-frame']"))
        # print("switch to iframe")
        # time.sleep(2)
        #
        # driver.find_element(By.XPATH, "//div[@class='demo']")
        # print("called div body, second frame, this frame contain speed,file,number,title")
        #

        driver.find_element(By.XPATH, "//span[@id='number-button']").click()
        print("after called div now clicked in select a speed button")
        # time.sleep(2)
        #
        # driver.find_element(By.XPATH, "//div[@class='ui-selectmenu-menu ui-front ui-selectmenu-open']")
        # print("after clicked speed button now call div class frame select-menu-open ")
        #
        # driver.find_element(By.XPATH, "//ul[@id='number-menu']")
        # print("after calling div class frame select-menu-open then call another frame div speed-menu")
        # print("then you click on options of speed-menu")
        #
        driver.find_element(By.XPATH, "//div[@class='ui-selectmenu-menu ui-front ui-selectmenu-open']//li[15]").click()
        print("option is 15")
        # time.sleep(2)
        #
        # # driver.find_element(By.XPATH, "//div[@id='ui-id-17']").click()
        # # print("option is 17")
        # # time.sleep(2)

        # SELECT NUMBER
        # driver.switch_to.frame(0)
        # print("switch to iframe")
        # time.sleep(2)

        # driver.find_element(By.XPATH, "//div[@class='demo']")
        # print("called div body, second frame, this frame contain speed,file,number,title")

        driver.find_element(By.XPATH, "//span[@id='salutation-button']").click()
        print("after called div now clicked in select a speed button")
        # time.sleep(2)


        # driver.execute_script("window.scrollTo(0,209)")
        # print("scrolled")
        # time.sleep(5)

        # actions = ActionChains(driver)
        # elm = driver.find_element(By.XPATH, "//div[@id='ui-id-6']")
        # actions.scroll_to_element(elm).perform()
        # time.sleep(5)

        # driver.find_element(By.XPATH, "//div[@class='ui-selectmenu-menu ui-front ui-selectmenu-open']")
        # print("after clicked speed button now call div class frame select-menu-open ")
        #
        # driver.find_element(By.XPATH, "(//ul[@id='salutation-menu'])[1]")
        # print("after calling div class frame select-menu-open then call another frame div speed-menu")
        # print("then you click on options of salutation-menu")
        #
        # driver.find_element(By.XPATH, "//div[@class='ui-selectmenu-menu ui-front ui-selectmenu-open']//li[3]").click()
        # print("option is li[3] = Mrs.")
        # time.sleep(2)
        # #
        driver.find_element(By.XPATH, "//div[@class='ui-selectmenu-menu ui-front ui-selectmenu-open']//li[6]").click()
        print("option is li[6] = others")
        # time.sleep(2)


testObj = Button()
testObj.test_button()
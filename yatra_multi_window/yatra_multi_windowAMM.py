#  যে window তে break দেয়া হবে সেই window আর handle করা যাবে না বাকিগুলা handle করা যাবে
#  একটি web/url থেকে new window open হয় তাহলে এইভাবে window handle করতে হয়
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


class SwitchTab():
    def multiple_tab_switch(self):
        executable_path = "I:\\Software Testing\\python\\rcvacademy\\Drivers\\chromedriver.exe"
        driver = webdriver.Chrome(executable_path)
        print('Browser launch success.')
        driver.maximize_window()
        driver.get('https://www.yatra.com/')
        print('Test URL open success.')

        parent_GUID = driver.current_window_handle
        print('parent GUID: ' + parent_GUID)

        driver.find_element(By.XPATH, "//a[normalize-space()='View All']").click()
        time.sleep(3)

        all_GUID = driver.window_handles
        print(all_GUID)

        # switch to child
        for child_guid in all_GUID:
            if child_guid not in parent_GUID:
                driver.switch_to.window(child_guid)
                parent_GUID = driver.current_window_handle
                print('parent GUID: ' + parent_GUID)
                driver.find_element(By.XPATH,
                                    "//a[@href='https://www.yatra.com/offer/details/zestmoney-offers']//span[@class='wfull offer-content anim']//img[@class='respnsiv-img']").click()
                time.sleep(8)
                for child_guid in all_GUID:
                    if child_guid not in parent_GUID:
                        driver.switch_to.window(child_guid)
                        # driver.find_element(By.XPATH, "//a[normalize-space()='Flat 12% OFF (up to Rs.1,600)']").click()
                        # print('After switch child Tab : ' + driver.title)
                        time.sleep(3)


                        break
                time.sleep(3)

                break
        driver.switch_to.window(parent_GUID)
        time.sleep(3)
        driver.switch_to.window(child_guid)
        time.sleep(3)
        driver.switch_to.window(child_guid)
        time.sleep(3)
        # switch to parent
        # for child_guid in all_GUID:
        #     if child_guid not in parent_GUID:
        #         driver.switch_to.window(parent_GUID)
        #         print('After switch parent Tab : ' + driver.title)
        #         time.sleep(3)
        # driver.find_element(By.XPATH, "//a[normalize-space()='View All']").click()
        # time.sleep(3)
        # driver.close()
        # driver.quit()

obj = SwitchTab()
obj.multiple_tab_switch()
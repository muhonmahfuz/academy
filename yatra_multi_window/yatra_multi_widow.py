#  যে window তে break দেয়া হবে সেই window আর handle করা যাবে না বাকিগুলা handle করা যাবে
#  একটি web/url থেকে new window open হয় তাহলে এইভাবে window handle করতে হয়
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By



class All():
    def test_all(self):
        executable_path= 'I:\\Software Testing\\python\\rcvacademy\\Drivers\\chromedriver.exe'
        driver = webdriver.Chrome(executable_path)
        print('Browser launch success.')
        driver.maximize_window()
        driver.get("https://www.yatra.com/")
        print('Test URL open success.')
        time.sleep(2)
        parent_handle=driver.current_window_handle
        print(parent_handle)
        viewall=driver.find_element(By.XPATH, "//a[normalize-space()='View All']")
        viewall.click()


        all_handles=driver.window_handles
        print(all_handles)
        for handle in all_handles:
            if handle != parent_handle:
                driver.switch_to.window(handle)
                #driver.find_element(By.XPATH, "//a[@href='https://www.yatra.com/offer/details/amazon-pay-icici-bank-card-offers']//span[@class='wfull offer-content anim']//img[@class='respnsiv-img']").click()
                time.sleep(4)

                break
        # driver.close(viewall)
        driver.switch_to.window(parent_handle)
        # print(parent_handle)
        # driver.find_element(By.XPATH, "//img[@alt='Flat 15% OFF (upto Rs.2,500)+ No Cost EMI on 3 months tenure']").click()
        # print('done')
        # time.sleep(2)
        # for handle1 in all_handles:
        #     if handle1 != parent_handle:
        #         driver.switch_to.window(handle1)
        #         # driver.find_element(By.XPATH, "//aside[@class='details-right']//li[3]").click()
        #         time.sleep(2)
        #         driver.close()
        #         time.sleep(5)
        #         break
        # driver.switch_to.window(parent_handle)
        # driver.find_element(By.XPATH, "//img[@alt='Flat 12% OFF (upto Rs. 1,500)']").click()
        # print('done')
        # time.sleep(2)











testObj = All()
testObj.test_all()
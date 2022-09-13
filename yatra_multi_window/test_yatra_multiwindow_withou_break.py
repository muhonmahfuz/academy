#  যে window তে break দেয়া হবে সেই window আর handle করা যাবে না বাকিগুলা handle করা যাবে
#  একটি web/url থেকে new window open হয় তাহলে এইভাবে window handle করতে হয়
import time
from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
# from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
import pytest
class Test_yatra:
    @pytest.fixture(scope="session")
    def setUp(self):
        global driver
        executable_path = "I:\\Software Testing\\python\\rcvacademy\\Drivers\\chromedriver.exe"
        driver = webdriver.Chrome(executable_path)
        driver.implicitly_wait(15)
        print('Browser launch success.')
        driver.maximize_window()


        yield
        driver.quit()
    def test_yatra_multi_window(self, setUp):
        global driver
        driver.get("https://www.yatra.com/")
        print('Test URL open success.')

        parent_handle = driver.current_window_handle
        print(parent_handle)

        viewall1 = driver.find_element(By.XPATH, "//a[normalize-space()='View All']")
        viewall1.click()
        time.sleep(2)

        all_handles = driver.window_handles
        print(all_handles)
        for handle1 in all_handles:
            if handle1 != parent_handle:
                driver.switch_to.window(handle1)
                driver.find_element(By.XPATH, "//a[@href='https://www.yatra.com/offer/details/citibank-emi-offers']//span[@class='wfull offer-content anim']//img[@class='respnsiv-img']").click()
                time.sleep(1)
                all_handles = driver.window_handles
                for extra01 in all_handles:
                    if extra01 != parent_handle:
                        driver.switch_to.window(extra01)

                driver.switch_to.window(handle1)
                time.sleep(1)
                driver.find_element(By.XPATH, "//a[@href='https://www.yatra.com/offer/details/citibank-emi-offers']//span[@class='wfull offer-content anim']//img[@class='respnsiv-img']").click()
                time.sleep(3)
                all_handles = driver.window_handles
                for extra02 in all_handles:
                    if extra02 != parent_handle:
                        driver.switch_to.window(extra02)
                # driver.find_element(By.XPATH, "//a[normalize-space()='Cabs']").click()
                # driver.find_element(By.XPATH, "//a[normalize-space()='Activity']").click()
                # break

        driver.switch_to.window(parent_handle)
        time.sleep(1)
        driver.switch_to.window(extra01)
        time.sleep(1)
        driver.switch_to.window(parent_handle)
        time.sleep(1)
        driver.switch_to.window(extra02)
        time.sleep(1)
        driver.switch_to.window(parent_handle)
        time.sleep(1)

        viewall2 = driver.find_element(By.XPATH, "//a[normalize-space()='View All']")
        viewall2.click()
        time.sleep(2)

        all_handles = driver.window_handles
        print(all_handles)
        for handle2 in all_handles:
            if handle2 != parent_handle:
                driver.switch_to.window(handle2)
                # driver.find_element(By.XPATH, "//a[normalize-space()='Bus']").click()
                # driver.find_element(By.XPATH, "//a[normalize-space()='Cabs']").click()
                # driver.find_element(By.XPATH, "//a[normalize-space()='Activity']").click()
                # driver.close()
                # break

        driver.switch_to.window(parent_handle)
        time.sleep(1)

        # driver.switch_to.window(handle2)
        # time.sleep(3)
        # driver.switch_to.window(handle1)
        # time.sleep(3)
        # driver.switch_to.window(parent_handle)
        # time.sleep(3)

        viewall3 = driver.find_element(By.XPATH, "//a[normalize-space()='View All']")
        viewall3.click()
        time.sleep(2)

        all_handles = driver.window_handles
        print(all_handles)
        for handle3 in all_handles:
            if handle3 != parent_handle:
                driver.switch_to.window(handle3)
                # driver.find_element(By.XPATH, "//a[normalize-space()='Bus']").click()
                # driver.find_element(By.XPATH, "//a[normalize-space()='Cabs']").click()
                # driver.find_element(By.XPATH, "//a[normalize-space()='Activity']").click()
                # driver.close()
                # break
        driver.switch_to.window(parent_handle)
        time.sleep(1)
        viewall4 = driver.find_element(By.XPATH, "//a[normalize-space()='View All']")
        viewall4.click()
        time.sleep(2)

        all_handles = driver.window_handles
        print(all_handles)
        for handle4 in all_handles:
            if handle4 != parent_handle:
                driver.switch_to.window(handle4)
                # driver.find_element(By.XPATH, "//a[normalize-space()='Bus']").click()
                # driver.find_element(By.XPATH, "//a[normalize-space()='Cabs']").click()
                # driver.find_element(By.XPATH, "//a[normalize-space()='Activity']").click()
                # driver.close()
                # break
        driver.switch_to.window(parent_handle)
        time.sleep(1)
        driver.switch_to.window(handle4)
        time.sleep(1)
        driver.switch_to.window(handle3)
        time.sleep(1)
        driver.switch_to.window(handle2)
        time.sleep(1)
        driver.switch_to.window(handle1)
        time.sleep(1)
        driver.switch_to.window(parent_handle)
        time.sleep(1)
        driver.switch_to.window(extra01)
        time.sleep(1)
        driver.switch_to.window(handle2)
        time.sleep(1)
        driver.switch_to.window(extra02)
        time.sleep(1)
        driver.switch_to.window(parent_handle)
        time.sleep(1)

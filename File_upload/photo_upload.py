import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_file():

    driver = webdriver.Chrome(executable_path="I:\\Software Testing\\python\\rcvacademy\\Drivers\\chromedriver.exe")
    driver.maximize_window()
    driver.implicitly_wait(15)
    driver.get("https://the-internet.herokuapp.com/upload")
    choosefile=driver.find_element(By.ID, "file-upload")
    choosefile.send_keys("C:/Users/Muhon PC/Desktop/Nid/habibur nid.jpeg")

    driver.find_element(By.ID, "file-submit").click()
    time.sleep(5)
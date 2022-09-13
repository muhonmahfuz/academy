import time
from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
# from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By


class All():
    def test_all(self):
        executable_path = "I:\\Software Testing\\python\\rcvacademy\\Drivers\\chromedriver.exe"
        driver = webdriver.Chrome(executable_path)
        print('Browser launch success.')
        driver.maximize_window()
        driver.get('https://youtube.com')
        print('Test URL open success.')
        time.sleep(1)
        # search Bar for povide input strings
        searchbar = driver.find_element(By.XPATH, "//input[@id='search']")
        searchbar.click()
        # this field is for type string
        searchbar.send_keys("E HAWA")
        time.sleep(1)
        # search button click Xpath
        searchbarbutton = driver.find_element(By.XPATH, "//button[@id='search-icon-legacy']//yt-icon[@class='style-scope ytd-searchbox']")
        searchbarbutton.click()
        time.sleep(1)
        #click and play first one on that list # common Xpath for all search result list
        driver.find_element(By.XPATH, "//body/ytd-app/div[@id='content']/ytd-page-manager[@id='page-manager']/ytd-search[@role='main']/div[@id='container']/ytd-two-column-search-results-renderer[@class='style-scope ytd-search']/div[@id='primary']/ytd-section-list-renderer[@class='style-scope ytd-two-column-search-results-renderer']/div[@id='contents']/ytd-item-section-renderer[@class='style-scope ytd-section-list-renderer']/div[@id='contents']/ytd-video-renderer[1]/div[1]").click()
        time.sleep(3)
        # click miniplayer
        driver.find_element(By.XPATH,"//button[@title='Miniplayer (i)']").click()
        searchbar
        searchbar.clear()
        searchbar.send_keys("Bokul fool")
        searchbarbutton.click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//body/ytd-app/div[@id='content']/ytd-page-manager[@id='page-manager']/ytd-search[@role='main']/div[@id='container']/ytd-two-column-search-results-renderer[@class='style-scope ytd-search']/div[@id='primary']/ytd-section-list-renderer[@class='style-scope ytd-two-column-search-results-renderer']/div[@id='contents']/ytd-item-section-renderer[@class='style-scope ytd-section-list-renderer']/div[@id='contents']/ytd-video-renderer[4]/div[1]").click()
        time.sleep(10)


testObj = All()
testObj.test_all()

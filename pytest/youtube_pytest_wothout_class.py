import time
from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
# from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
import pytest

@pytest.fixture(scope="module")
def setUp():
    global driver
    executable_path = "I:\\Software Testing\\python\\rcvacademy\\Drivers\\chromedriver.exe"
    driver = webdriver.Chrome(executable_path)
    driver.implicitly_wait(15)
    print('Browser launch success.')
    driver.maximize_window()
    driver.get('https://youtube.com')
    print('Test URL open success.')

    yield
    driver.close()

def test_song_search(setUp):
    driver.get('https://youtube.com')
    print('Test URL open success.')
    # search Bar for povide input strings
    searchbar = driver.find_element(By.XPATH, "//input[@id='search']")
    searchbar.click()
    # this field is for type string
    searchbar.send_keys("E HAWA")
    # time.sleep(1)
    # search button click Xpath
    searchbarbutton = driver.find_element(By.XPATH, "//button[@id='search-icon-legacy']//yt-icon[@class='style-scope ytd-searchbox']")
    searchbarbutton.click()
    # time.sleep(1)
    #click and play first one on that list
    driver.find_element(By.XPATH, "//body/ytd-app/div[@id='content']/ytd-page-manager[@id='page-manager']/ytd-search[@role='main']/div[@id='container']/ytd-two-column-search-results-renderer[@class='style-scope ytd-search']/div[@id='primary']/ytd-section-list-renderer[@class='style-scope ytd-two-column-search-results-renderer']/div[@id='contents']/ytd-item-section-renderer[@class='style-scope ytd-section-list-renderer']/div[@id='contents']/ytd-video-renderer[1]/div[1]").click()
    # time.sleep(3)
    # click miniplayer
    driver.find_element(By.XPATH,"//button[@title='Miniplayer (i)']").click()
    searchbar
    searchbar.clear()
    searchbar.send_keys("Bokul fool")
    searchbarbutton.click()
    # time.sleep(1)
    driver.find_element(By.XPATH, "//body/ytd-app/div[@id='content']/ytd-page-manager[@id='page-manager']/ytd-search[@role='main']/div[@id='container']/ytd-two-column-search-results-renderer[@class='style-scope ytd-search']/div[@id='primary']/ytd-section-list-renderer[@class='style-scope ytd-two-column-search-results-renderer']/div[@id='contents']/ytd-item-section-renderer[@class='style-scope ytd-section-list-renderer']/div[@id='contents']/ytd-video-renderer[1]/div[1]").click()
    # time.sleep(10)
def test_youtube_Scroll(setUp):
    driver.get('https://youtube.com')
    print('Test URL open success.')
    elmt1=driver.find_element(By.XPATH, "//div[@id='title-text']//span[@id='title']")
    # elmt1.click()
    actions = ActionChains(driver)
    actions.scroll_to_element(elmt1).perform()
    # time.sleep(10)
def test_youtube_guid(setUp):
    driver.get('https://youtube.com')
    print('Test URL open success.')
    guidbar= driver.find_element(By.XPATH, "//div[@id='start']//yt-icon[@id='guide-icon']")
    guidbar.click()
    # time.sleep(2)
    guidbar.click()
    # time.sleep(2)
# def test_youtube1(setUp):
#
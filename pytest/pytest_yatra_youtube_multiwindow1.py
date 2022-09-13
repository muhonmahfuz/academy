import time
from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
# from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
import pytest
class Test_youtube_pytest:
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

    #@pytest.mark.skip
    def test_song_search(self,setUp):
        driver.get('https://youtube.com')
        print('Test URL open success.')
        # search Bar for povide input strings
        searchbar = driver.find_element(By.XPATH, "//input[@id='search']")
        searchbar.click()
        # this field is for type string
        searchbar.send_keys("E HAWA")
        # # time.sleep(1)
        # search button click Xpath
        # searchbarbutton = driver.find_element(By.XPATH, "//button[@id='search-icon-legacy']//yt-icon[@class='style-scope ytd-searchbox']")
        # searchbarbutton.click()
        # time.sleep(1)
        #click and play first one on that list
        # driver.find_element(By.XPATH, "//body/ytd-app/div[@id='content']/ytd-page-manager[@id='page-manager']/ytd-search[@role='main']/div[@id='container']/ytd-two-column-search-results-renderer[@class='style-scope ytd-search']/div[@id='primary']/ytd-section-list-renderer[@class='style-scope ytd-two-column-search-results-renderer']/div[@id='contents']/ytd-item-section-renderer[@class='style-scope ytd-section-list-renderer']/div[@id='contents']/ytd-video-renderer[1]/div[1]").click()
        # # time.sleep(3)
        # # click miniplayer
        # driver.find_element(By.XPATH,"//button[@title='Miniplayer (i)']").click()
    #     searchbar
    #     searchbar.clear()
    #     searchbar.send_keys("Bokul fool")
    #     searchbarbutton.click()
    #     # time.sleep(1)
    #     driver.find_element(By.XPATH, "//body/ytd-app/div[@id='content']/ytd-page-manager[@id='page-manager']/ytd-search[@role='main']/div[@id='container']/ytd-two-column-search-results-renderer[@class='style-scope ytd-search']/div[@id='primary']/ytd-section-list-renderer[@class='style-scope ytd-two-column-search-results-renderer']/div[@id='contents']/ytd-item-section-renderer[@class='style-scope ytd-section-list-renderer']/div[@id='contents']/ytd-video-renderer[1]/div[1]").click()
    #     # time.sleep(10)
    #@pytest.mark.skip
    def test_youtube_Scroll(self,setUp):
        driver.get('https://youtube.com')
        print('Test URL open success.')
        elmt1=driver.find_element(By.XPATH, "//div[@id='title-text']//span[@id='title']")
        # elmt1.click()
        actions = ActionChains(driver)
        actions.scroll_to_element(elmt1).perform()
        # time.sleep(10)

    @pytest.mark.skip
    def test_youtube_guid(self,setUp):
        driver.get('https://youtube.com')
        print('Test URL open success.')
        guidbar= driver.find_element(By.XPATH, "//div[@id='start']//yt-icon[@id='guide-icon']")
        guidbar.click()
        # time.sleep(2)
        guidbar.click()
        # time.sleep(2)
    # def test_youtube1(setUp):

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

    @pytest.mark.skip
    def test_yatra_checkbox(self,setUp):
        driver.get('https://www.yatra.com/')
        # print('the title is :' + driver.title)
        # print('Test URL open success.')
        driver.find_element(By.XPATH, "//a[@title='Non Stop Flights']").click()

        print("select non stop flights")
        driver.find_element(By.XPATH, "//a[@title='Non Stop Flights']").click()

        print("deselect non stop flights")
        driver.find_element(By.XPATH, "//a[@title='Student Fare Offer']").click()

        print("select student fare")
        driver.find_element(By.XPATH, "//a[@title='Student Fare Offer']").click()

        print("deselect student fare")
        driver.find_element(By.XPATH, "//a[@title='Armed Forces Offer']").click()

        print("select armed forches")


    def test_yatra_mainpage(self, setUp):
        driver.get('https://www.yatra.com/')
        moreoption = driver.find_element(By.XPATH, "//span[@class='more-arr']")

        actions = ActionChains(driver)
        actions.move_to_element(moreoption).perform()


        trains = driver.find_element(By.XPATH, "//span[normalize-space()='Trains']")
        trains.click()


        driver.execute_script("")

        alert = driver.find_element(By.XPATH, "//button[normalize-space()='OK']")

        alert.click()
        print("done")

    def test_yatra_forbusiness(self, setUp):
        driver.get("https://www.yatra.com/")
        print('Test URL open success.')

        parent_handle = driver.current_window_handle
        print(parent_handle)
        viewall = driver.find_element(By.XPATH, "//a[normalize-space()='View All']")
        viewall.click()

        all_handles = driver.window_handles
        print(all_handles)
        for handle in all_handles:
            if handle != parent_handle:
                driver.switch_to.window(handle)
                driver.find_element(By.XPATH, "//a[normalize-space()='Bus']").click()
                driver.find_element(By.XPATH, "//a[normalize-space()='Cabs']").click()
                driver.find_element(By.XPATH, "//a[normalize-space()='Activity']").click()
                driver.close()
                break
        driver.switch_to.window(parent_handle)
    def test_yatra_viewall(self, setUp):
        # driver.get("https://www.yatra.com/")
        driver.get('https://www.yatra.com/offer/dom/listing/domestic-flight-deals')
        # driver.find_element(By.XPATH, "//a[normalize-space()='View All']").click()
        driver.find_element(By.XPATH, "//a[normalize-space()='Bus']").click()
        driver.find_element(By.XPATH, "//a[normalize-space()='Cabs']").click()
        driver.find_element(By.XPATH, "//a[normalize-space()='Activity']").click()

    def test_yatra_dropdown(self, setUp):
        driver.get('https://www.yatra.com/')
        # print('the title is :' + driver.title)
        # print('Test URL open success.')

        driver.find_element(By.XPATH, "//span[normalize-space()='Holidays']").click()
        print("clicked holiday option")

        monthoftravel = driver.find_element(By.XPATH, "//div[@class='ddTitle borderRadiusTp holi_passengerBox']")
        monthoftravel.click()

        driver.find_element(By.XPATH, "//div[@class='overview']")
        print("called all option frame_ div overview")

        driver.find_element(By.XPATH, "//span[normalize-space()='October 2022']").click()
        print("than clicked on option from all option frame 'October 2022'")

    def test_yatra_radiobutton(self, setUp):
        driver.get('https://www.yatra.com/')
        multicity = driver.find_element(By.XPATH, "//a[@title='Multicity']")
        multicity.click()
        print("click on Multicity")


        traveller = driver.find_element(By.XPATH, "//span[normalize-space()='Traveller']")
        traveller.click()
        print("click on Traveller")
        time.sleep(2)

        business = driver.find_element(By.XPATH, "//span[normalize-space()='Business']")
        business.click()
        print("click on Business")


        economy = driver.find_element(By.XPATH, "//span[normalize-space()='Economy']")
        economy.click()
        print("select Economy")


        premium_economy = driver.find_element(By.XPATH, "//span[normalize-space()='Premium Economy']")
        premium_economy.click()
        print("click on premium_economy")


        non_stop_flights = driver.find_element(By.XPATH, "//a[@title='Non Stop Flights']")
        non_stop_flights.click()
        print("click on non_stop_flights")


        non_stop_flights.click()
        print("click on non stop flight for deselect")


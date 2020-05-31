from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import unittest #for automated testing
from time import sleep


class VagaryTesting(unittest.TestCase):
    @classmethod

    def setUpClass(self): 
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        print("setup driver")
        
    #test if the correct page loads with the correct title
    def test01(self):
        self.driver.get("http://localhost:5000")
        sleep(3)
        assert self.driver.title == "Vagary"
        sleep(2)
    
    #test if recomendations work
    def test02(self):
        self.driver.get("http://localhost:5000/login")
        user = self.driver.find_element_by_name("username")
        password = self.driver.find_element_by_name("pass")
        user.send_keys("richa123")
        sleep(1)
        password.send_keys("richa123")
        password.send_keys(Keys.RETURN)
        sleep(10)
        place = self.driver.find_element_by_name("reco1")
        ht1 = place.get_attribute("innerHTML")
        assert ht1 == "Malaysia"

    def test03(self):
        self.driver.get("http://localhost:5000/login")
        user = self.driver.find_element_by_name("username")
        password = self.driver.find_element_by_name("pass")
        user.send_keys("riya")
        sleep(1)
        password.send_keys("riya123")
        password.send_keys(Keys.RETURN)
        sleep(10)
        place = self.driver.find_element_by_name("reco1")
        ht1 = place.get_attribute("innerHTML")
        assert ht1 == "Cayman Islands"

    #test if booknow works
    def test04(self):
        self.driver.get("http://localhost:5000/about")
        sleep(2)
        button = self.driver.find_element_by_name("booknow").click()
        sleep(4)
        assert self.driver.title == "Search"

    #test if logo works
    def test05(self):
        self.driver.get("http://localhost:5000/about")
        sleep(2)
        logo = self.driver.find_element_by_id("logo").click()
        sleep(2)
        assert self.driver.title == "Home"

    #test if continents work
    def test06(self):
        self.driver.get("http://localhost:5000/home")
        sleep(3)
        asia = self.driver.find_element_by_id("asia").click()
        sleep(2)
        assert self.driver.title == "top places to visit in asia - Google Search"
        sleep(1)
        self.driver.get("http://localhost:5000/home")
        sleep(2)
        america = self.driver.find_element_by_id("america").click()
        sleep(1)
        assert self.driver.title == "top places to visit in america - Google Search"
        
    #test social media
    def test07(self):
        self.driver.get("http://localhost:5000/home")
        sleep(4)
        btnfb = self.driver.find_element_by_name("fb").click()
        sleep(1)
        try:
            fb = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "pageTitle"))).text
            facebook = fb.get_attribute("innerHTML")
            assert facebook == "Facebook - log in or sign up"
        except TimeoutException:
            assert "Error"
        self.driver.get("http://localhost:5000/home")
        sleep(2)
        btninst = self.driver.find_element_by_name("insta").click()
        sleep(1)
        assert self.driver.title == "Instagram"
        sleep(1)


    #test if search works    
    def test08(self):
        self.driver.get("http://localhost:5000/search")
        place = self.driver.find_element_by_id("place")
        place.send_keys("Barcelona")
        search = self.driver.find_element_by_id("btnsearch").click()
        sleep(2)
        try:
            heading = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "hotels")))
            hotel = heading.get_attribute("innerHTML")
            assert hotel == "Hotels in Barcelona"
        except TimeoutException:
            assert "Error!"
        sleep(5)

    #test if book button works
    def test09(self):
        self.driver.get("http://localhost:5000/search")
        place = self.driver.find_element_by_id("place")
        place.send_keys("Barcelona")
        sleep(2)
        button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, 'btnsearch')))
        button.click()
        sleep(3)
        try:
            book = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, 'btn1')))
            book.click()
            sleep(8)
            hotel = self.driver.find_element_by_name("place1b")
            name = hotel.get_attribute("innerHTML")
            sleep(3)
            assert name == "Autohogar Hotel Barcelona"
        except TimeoutException:
            assert "Error!"

    #test if booking can be done
    def test10(self):
        self.driver.get("http://localhost:5000/search")
        place = self.driver.find_element_by_id("place")
        place.send_keys("Barcelona")
        sleep(1)
        button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, 'btnsearch')))
        button.click()
        sleep(1)
        try:
            book = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, 'btn1')))
            book.click()
            sleep(2)
            checkin = self.driver.find_element_by_id("datepicker_1")
            checkin.send_keys("01062020")
            sleep(1)
            checkout = self.driver.find_element_by_id("datepicker_2")
            checkout.send_keys("07062020")
            sleep(1)
            rooms = self.driver.find_element_by_id("per")
            rooms.send_keys("2")
            sleep(1)
            accept = self.driver.find_element_by_id("accept")
            accept.click()
            h1 = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "success")))
            # h1 = self.driver.find_element_by_id("success")
            success = h1.get_attribute("innerHTML")
            sleep(3)
            assert success == "Successful Booking!!!"
        except TimeoutException:
            assert "Error!"

    #test other pages and book now
    def test11(self):
        self.driver.get("http://localhost:5000/home")
        sleep(1)
        try:
            dropdown= WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, 'navbarDropdown_1'))).click()
            sleep(1)
            topplace =WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, 'topplace'))).click()
            sleep(4)
            dropdown= WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, 'navbarDropdown_1'))).click()
            sleep(5)
            tourdetails =WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, 'tourdetails'))).click()
            sleep(5)
            booktix =WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, 'bt'))).click()
            sleep(5)
            assert self.driver.title == "Search"
        except TimeoutException:
            assert "Error"
        
    @classmethod
    def tearDownClass(self):
        self.driver.close()


#provides command line interface to test script
if __name__ == '__main__': 
    unittest.main()


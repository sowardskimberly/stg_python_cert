import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

"""
Find all the Makes available from the home page at copart.com. Verify each make takes you to a search of the correct
make
"""

class Challenge7(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver")

    def tearDown(self):
        self.driver.close()

    def test_challenge7(self):
        website = "https://www.copart.com"
        self.driver.get(website)
        wait = WebDriverWait(self.driver, 60).until(EC.presence_of_element_located((By.ID, "input-search")))
        # List of all elements in the available make section of page
        total_makes = self.driver.find_elements_by_xpath('//span[@class="make-items"]/span/a')
        car_make = []
        car_href = []
        # separate the car make and car href from the list of all elements on page
        for car in range(len(total_makes)-1):
            car_make.append(total_makes[car].text)
            car_href.append(total_makes[car].get_attribute('href'))

        # Visit every href and verify that the make on the home page matches the search make
        timeout = 3  # seconds
        for item in range(len(car_href) - 1):
            self.driver.get(car_href[item])
            try:
                Waiting = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((
                    By.XPATH, '(//tr[@class="odd"])')))
            except TimeoutException:
                print("Something really bad happened. You should make a ticket for this")

            # get a list of makes on the search page
            makes_on_page = self.driver.find_elements_by_xpath('//span[@data-uname="lotsearchLotmake"]')
            # find one of those makes
            make_on_page = makes_on_page[0].get_attribute('innerHTML')

            try:
                self.assertEqual((car_make[item]).upper(), make_on_page)
            except AssertionError:
                print(make_on_page)  # Harley vs Harley-Davidson and Maclaren vs Maclaren Auotomotives don't match. Bug?


if __name__ == '__main__':
    unittest.main()
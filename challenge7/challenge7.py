import unittest
from selenium import webdriver
import os
import sys
from libs import Cars

# Add current directory to import a file used in all challenge folders
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)


class Challenge7(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver")

    def tearDown(self):
        self.driver.close()

    def test_challenge7(self):
        """On Copart navigate check that the make list navigates to a page with that make on it
        """
        website = "https://www.copart.com"
        Cars.navigate_to_copart(website, self.driver)
        car_make, car_href = Cars.sep_makes_and_href(self.driver)
        Cars.go_to_links(car_make, car_href, self.driver)


if __name__ == '__main__':
    unittest.main()

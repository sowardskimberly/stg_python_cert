import unittest
from selenium import webdriver
from library.libs import Cars


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

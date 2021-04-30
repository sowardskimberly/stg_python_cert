import unittest
from selenium import webdriver
from library.libs import Cars


class Challenge6(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver")

    def tearDown(self):
        self.driver.close()

    def test_challenge6(self):
        """Search for a make, then an unpopular model. If the model isn't listed catch the error
        and take a screen shot of the page, otherwise let us know if it was there
        """

        # define variables
        website = "https://www.copart.com"
        make_text = "nissan"
        model_text = "skyline"
        Cars.navigate_to_copart(website, self.driver)
        # Search for text in main search bar
        Cars.searchbar_search(make_text, self.driver)
        # Open a filter on the left side
        Cars.open_filter("model", self.driver)
        # Search for model
        Cars.model_search(model_text, self.driver)


if __name__ == '__main__':
    unittest.main()

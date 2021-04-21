import unittest
from selenium import webdriver
import os
import sys
from libs import Cars

# Add current directory to import a file used in all challenge folders
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)


class Challenge5(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver")

    def tearDown(self):
        self.driver.close()

    def test_challenge5(self):
        """Count how many of each type of model shows on the first page
        Then count how many unique damage types exist"""

        website = "https://www.copart.com"
        search_text = "porsche"
        Cars.navigate_to_copart(website, self.driver)
        Cars.searchbar_search(search_text, self.driver)
        Cars.twenty_to_hundred(self.driver)
        model_list_cars = Cars.visible_makes(self.driver)
        unique_list_models = Cars.unique_values(model_list_cars)
        Cars.unique_counter(unique_list_models, model_list_cars)

        # Second part count the number of different damage types
        Cars.count_damages(self.driver)


if __name__ == '__main__':
    unittest.main()

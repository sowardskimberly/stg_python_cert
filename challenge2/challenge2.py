import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class Challenge2(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver")

    def tearDown(self):
        self.driver.close()

    def test_challenge2(self):
        """Open copart.com and search for exotics. In the list verify that porsche is an option
        """
        website = "https://www.copart.com"
        search_word = "exotics"
        self.driver.get(website)
        # I had to wait or else the next find_element would have zero results
        wait = WebDriverWait(self.driver, 60).until(EC.presence_of_element_located((By.ID, "input-search")))

        search_block = self.driver.find_element_by_id("input-search")
        search_block.send_keys(search_word, Keys.ENTER)

        # Next find_elements_by was searching before the table loaded. Added a wait so table could load
        # This wait assumes that the search has matching values
        wait = WebDriverWait(self.driver, 60).until(EC.presence_of_element_located((By.XPATH, "//tr[@role = 'row']")))
        element_found = True
        try:
            self.driver.find_elements_by_xpath('//span[text() = "PORSCHE"]')
        except NoSuchElementException:
            element_found = False

        self.assertEqual(element_found, True)


if __name__ == '__main__':
    unittest.main()

import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Challenge3(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver")

    def tearDown(self):
        self.driver.close()

    def test_challenge3(self):
        """Go to copart.com and search through popular items. Return the make the url for each popular item
        """
        website = "https://www.copart.com"
        self.driver.get(website)
        # I had to wait or else the next find_element would have zero results
        wait = WebDriverWait(self.driver, 60).until(EC.presence_of_element_located((By.ID, "input-search")))
        total_populars = self.driver.find_elements_by_xpath('//div[@ng-if="popularSearches"]//ul/li/a')
        print('for loop')
        for i in total_populars:
            attribute = i.get_attribute('innerHTML')
            href_website = i.get_attribute('href')
            print(attribute + " - " + href_website)

        # try while loop
        print('while loop')
        count = 0
        while count < len(total_populars):
            attribute = total_populars[count].get_attribute('innerHTML')
            href_website = total_populars[count].get_attribute('href')
            print(attribute + " - " + href_website)
            count = count + 1


if __name__ == '__main__':
    unittest.main()

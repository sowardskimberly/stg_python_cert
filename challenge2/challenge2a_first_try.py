import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Challenge2(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver")

    def tearDown(self):
        self.driver.close()

    def test_challenge2(self):
        self.driver.get("https://www.copart.com")
        self.driver.implicitly_wait(60)
        mydynamicelement = self.driver.find_element_by_xpath(('(//input[@type = "text"])[1]'))

        search_block = self.driver.find_element_by_xpath(('(//input[@type = "text"])[1]'))
        self.driver.implicitly_wait(50)  # seconds
        search_block.send_keys("exotics", Keys.ENTER)
        mydynamicelement = self.driver.find_elements_by_xpath('//tr[@role = "row"]')



        element_found = True;
        try:
            self.driver.find_elements_by_xpath('//span[text() = "PORSCHE"]')
        except:
            element_found = False


        self.assertEqual(element_found, True)


if __name__ == '__main__':
    unittest.main()
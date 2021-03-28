import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


"""
Go to copart.com and search for a rare car. If it doesn't have a listing take a screen shot of the page
and store the screenshot. If it is there it tells us it is there
"""


class Challenge6(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver")

    def tearDown(self):
        self.driver.close()

    def test_challenge6(self):
        # navigate to website
        website = "https://www.copart.com"
        search_text = "nissan skyline"
        self.driver.get(website)
        wait = WebDriverWait(self.driver, 60).until(EC.presence_of_element_located((By.ID, "input-search")))
        search_block = self.driver.find_element_by_id("input-search")

        # Enter search in
        search_block.send_keys(search_text, Keys.ENTER)

        # this is what I had to do to get it to wait for the table or lack of table to load. I couldn't find
        # a similar feature on the page if it had a result vs if it did not have a result. I start with waiting
        # to find if the table exist (a result exists) and if it can't find it then it assumes the table didn't load
        # because there is no result for the search. I don't love it because it makes it statically wait 3 seconds
        # if there is no result, but this was the only way I could get it to recognize the right answer of there being
        # a skyline available or not
        timeout = 3  # seconds
        try:
            Waiting = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.XPATH,
                '(//span[text() = "SKYLINE"])[1]')))
            print('Look a Skyline!')
        except TimeoutException:
            print("No skyline's available right now")
            self.driver.save_screenshot('no_nissan_skyline.png')


if __name__ == '__main__':
    unittest.main()

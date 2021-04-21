import unittest
from selenium import webdriver


class Challenge1(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver")

    def tearDown(self):
        self.driver.close()

    def test_challenge1(self):
        """Open Google and assert that the title is google
        """
        website = "https://www.google.com"
        self.driver.get(website)
        self.assertIn("Google", self.driver.title)


if __name__ == '__main__':
    unittest.main()

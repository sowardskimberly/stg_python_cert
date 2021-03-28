import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException
from pprint import pprint

"""
First part goes to copart.com and searches for porches. Then we change the search from 20 to 100. 
We then count how many different models of porches are available and count how many of each exist

Second part uses a switch case in python to count the types of damages on all the porsches listed
"""


class Challenge5(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver")

    def tearDown(self):
        self.driver.close()

    def test_challenge5(self):
        website = "https://www.copart.com"
        search_text = "porsche"
        self.driver.get(website)
        # had to wait for search bar to load or else next find_by_element would fail
        wait = WebDriverWait(self.driver, 60).until(EC.presence_of_element_located((By.ID, "input-search")))
        search_block = self.driver.find_element_by_id("input-search")

        # Enter search in to find cars that are porches
        search_block.send_keys(search_text, Keys.ENTER)
        wait = WebDriverWait(self.driver, 60).until(EC.presence_of_all_elements_located(
            (By.XPATH, "//tr[@role = 'row']")))

        # change filter to 100 from 20
        dropdown = self.driver.find_element_by_xpath("//option[. = '100']").click()
        # I had to wait or else I had no results, but this seems fragile.
        # It assumes there is a table and that there are 100 items in that table
        wait = WebDriverWait(self.driver, 60).until(
            EC.presence_of_all_elements_located((By.XPATH, '(//span[@data-uname = "lotsearchLotmodel"])[101]')))

        # make array from all the values in the xpaths, then sort alphabetically
        model_array = self.driver.find_elements_by_xpath('//span[@data-uname = "lotsearchLotmodel"]')
        models_list = []
        for listing in range(len(model_array) - 1):
            try:
                models_list.append(model_array[listing].text)
            except StaleElementReferenceException:  # used to get an error of sale elements now I don't
                print('StaleElementReferenceException while getting all models, trying again')
                model_array = self.driver.find_elements_by_xpath('//span[@data-uname = "lotsearchLotmodel"]')
                models_list = model_array[listing].text
        models_list.sort()

        # Make a list of the unique models
        unique_list = []
        for model in models_list:
            if model not in unique_list:
                unique_list.append(model)

        # count number of unique values in the total list
        total_number = []
        for unique_model in unique_list:
            total_number.append(models_list.count(unique_model))

        # print number of unique values
        print("Number of unique models: " + str(len(unique_list)))
        # print the similar values
        for final_modal in range(len(unique_list)):
            print(unique_list[final_modal] + ": " + str(total_number[final_modal]) + " count")

        # Second part of challenge. Use a python switch statement to count the types of damages on the porsches

        car_damages = {
            'REAR END': 0,
            'FRONT END': 0,
            'MINOR DENT/SCRATCHES': 0,
            'UNDERCARRIAGE': 0,
            'MISC': 0
        }

        damage_array = self.driver.find_elements_by_xpath('//span[@data-uname = "lotsearchLotdamagedescription"]')
        # Find text in values in the xpaths and add counts for each damage type
        for car in damage_array:
            damage = car.text
            if damage in car_damages.keys():
                car_damages[damage] += 1
            else:
                car_damages['Misc'] += 1

        print()
        print("Types of damages")
        pprint(car_damages)


if __name__ == '__main__':
    unittest.main()
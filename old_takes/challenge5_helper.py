from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException
from pprint import pprint


class Cars:

    def __init__(self, search_text, model):
        pass

    @classmethod
    def navigate_to_copart(cls, website, driver_info):
        """
                Navigates to a copart and waits for copart to load

                args:
                website (str): string of a website url
                driver_info (driver): the browser being used
                """

        # specifically waits for copart to load
        driver_info.get(website)
        wait = WebDriverWait(driver_info, 60).until(EC.presence_of_element_located((By.ID, "input-search")))

    @classmethod
    def searchbar_search(cls, search, driver_info):
        """
        Sends keys in search bar and waits for table to load

        args:
            search (str): value being searched
            driver_info (driver): the browser being used
        """
        cls.search_text = search
        search_block = driver_info.find_element_by_id("input-search")
        search_block.send_keys(search, Keys.ENTER)
        wait = WebDriverWait(driver_info, 60).until(EC.presence_of_element_located((By.XPATH,
            '//li[@class = "list-group-item"]')))

    @classmethod
    def twenty_to_hundred(cls, driver_info):
        dropdown = driver_info.find_element_by_xpath("//option[. = '100']").click()
        # It assumes there is a table and that there is at least 1 items in that table
        wait = WebDriverWait(driver_info, 60).until(
            EC.presence_of_all_elements_located((By.XPATH, '(//span[@data-uname = "lotsearchLotmodel"])[2]')))

    @classmethod
    def visible_makes(cls, driver_info):
        # make array from all the values in the xpaths, then sort alphabetically
        model_array = driver_info.find_elements_by_xpath('//span[@data-uname = "lotsearchLotmodel"]')
        models_list = []
        for listing in range(len(model_array) - 1):
            try:
                models_list.append(model_array[listing].text)
            except StaleElementReferenceException:  # used to get an error of sale elements now I don't
                print('StaleElementReferenceException while getting all models, trying again')
                model_array = driver_info.find_elements_by_xpath('//span[@data-uname = "lotsearchLotmodel"]')
                models_list.append(model_array[listing].text)
        models_list.sort()
        return models_list

    @staticmethod
    def unique_values(some_list):
        unique_list = []
        for model in some_list:
            if model not in unique_list:
                unique_list.append(model)
        return unique_list

    @staticmethod
    def unique_counter(unique_list, models_list):
        # count number of unique values in the total list
        total_number = []
        for unique_model in unique_list:
            total_number.append(models_list.count(unique_model))

        # print number of unique values
        print("Number of unique models: " + str(len(unique_list)))
        # print the similar values
        for final_modal in range(len(unique_list)):
            print(unique_list[final_modal] + ": " + str(total_number[final_modal]) + " count")

    @classmethod
    def count_damages(cls, driver_info):
        # Second part of challenge. Use a python switch statement to count the types of damages on the porsches

        car_damages = {
            'REAR END': 0,
            'FRONT END': 0,
            'MINOR DENT/SCRATCHES': 0,
            'UNDERCARRIAGE': 0,
            'MISC': 0
        }

        damage_array = driver_info.find_elements_by_xpath('//span[@data-uname = "lotsearchLotdamagedescription"]')
        # Find text in values in the xpaths and add counts for each damage type
        for car in damage_array:
            damage = car.text
            if damage in car_damages.keys():
                car_damages[damage] += 1
            else:
                car_damages['MISC'] += 1

        print()
        print("Types of damages")
        pprint(car_damages)

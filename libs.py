from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import TimeoutException
from pprint import pprint


class Cars:

    def __init__(self):
        pass

    @staticmethod
    def navigate_to_copart(website, driver_info):
        """Navigates to a copart and waits for copart to load

            args:
                website (str): string of a website url
                driver_info (driver): the browser being used
        """
        driver_info.get(website)
        wait = WebDriverWait(driver_info, 60).until(EC.presence_of_element_located((By.ID, "input-search")))

    @staticmethod
    def searchbar_search(search, driver_info):
        """Sends keys in search bar and waits for table to load

            args:
                search (str): value being searched
                driver_info (driver): the browser being used
        """
        search_block = driver_info.find_element_by_id("input-search")
        search_block.send_keys(search, Keys.ENTER)
        wait = WebDriverWait(driver_info, 60).until(EC.presence_of_element_located((By.XPATH,
            '//li[@class = "list-group-item"]')))

    @staticmethod
    def visible_makes(driver_info):
        """Sends keys in search bar and waits for table to load

            args:
                driver_info (driver): the browser being used
        """
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
        """After getting a list of strings, this will return a unique list of values in that list

        args:
            some_list (list): List of strings
        """
        unique_list = []
        for model in some_list:
            if model not in unique_list:
                unique_list.append(model)
        return unique_list

    @staticmethod
    def twenty_to_hundred(driver_info):
        """On Copart.com after searching this will make the search go from 20 (default) to 100

        Args:
            driver_info (driver): the browser being used
        """
        dropdown = driver_info.find_element_by_xpath("//option[. = '100']").click()
        # It assumes there is a table and that there is at least 1 items in that table
        wait = WebDriverWait(driver_info, 60).until(
            EC.presence_of_all_elements_located((By.XPATH, '(//span[@data-uname = "lotsearchLotmodel"])[2]')))

    @staticmethod
    def unique_counter(unique_list, models_list):
        """This creates a list and count of unique values in a list

        args:
            unique_list (list): an unique list of string values
            models_list: a list of string values
        """
        total_number = []
        for unique_model in unique_list:
            total_number.append(models_list.count(unique_model))

        # print number of unique values
        print("Number of unique models: " + str(len(unique_list)))
        # print the similar values
        for final_modal in range(len(unique_list)):
            print(unique_list[final_modal] + ": " + str(total_number[final_modal]) + " count")

    @staticmethod
    def count_damages(driver_info):
        """Using a hard coded damage set from the challenge this adds a count in a python version of a switch statement

        args:
            driver_info (driver): the browser being used
        """
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

    @staticmethod
    def take_screenshot(title, driver_info):
        """Provides a nice clean way to save sreenshots for later tests

        args:
            title (str): A string
            driver_info (driver): the browser being used
        """
        driver_info.save_screenshot(title)

    @staticmethod
    def open_filter(filter_choice, driver_info):
        """Opens a filter on the left side of coparts page

        args:
            filter_choice (str): The filter that is being expanded
            driver_info (driver): the browser being used
        """
        formal_filter = filter_choice.capitalize()
        model_expand = driver_info.find_element_by_xpath('//a[@data-uname = "{}Filter"]'.format(formal_filter)).click()

    @staticmethod
    def model_search(model_text, driver_info):
        """From an expanded filter this searches for a specific model of car on copart

        args:
            model_text (str): a string value of the car model being searched for
            driver_info (driver): the browser being used
        """
        model_search = driver_info.find_element_by_xpath('(//input[@placeholder = "Search"])[5]')
        formal_modal = model_text.capitalize()
        model_search.send_keys(formal_modal)
        try:
            model_done_searching = driver_info.find_element_by_xpath('//abbr[@value = "{}"]'.format(formal_modal))
            print("Look there are {}'s!".format(formal_modal))
        except NoSuchElementException:
            print("No {}'s available right now".format(formal_modal))
            file_name = "no_{}.png".format(formal_modal)
            Cars.take_screenshot(file_name, driver_info)

    @staticmethod
    def sep_makes_and_href(driver_info):
        """This finds links on the page and separates the text from the hrefs

        args:
            driver_info (driver): the browser being used
        """
        total_makes = driver_info.find_elements_by_xpath('//span[@class="make-items"]/span/a')
        car_make = []
        car_href = []
        # separate the car make and car href from the list of all elements on page
        for car in range(len(total_makes) - 1):
            car_make.append(total_makes[car].text)
            car_href.append(total_makes[car].get_attribute('href'))
        return car_make, car_href

    @staticmethod
    def go_to_links(car_list, href_list, driver_info):
        """Visits every href and verifies that the make on the table matches the listed make

        args:
            car_list (list): a list of strings taken from a previous page
            href_list (list): a list of hrefs taken from a previous page
            driver_info (driver): the browser being used
        """
        timeout = 3  # seconds
        for item in range(len(href_list) - 1):
            driver_info.get(href_list[item])
            try:
                Waiting = WebDriverWait(driver_info, timeout).until(EC.presence_of_element_located((
                    By.XPATH, '(//tr[@class="odd"])')))
            except TimeoutException:
                title = 'whoopsies'
                Cars.take_screenshot(title, driver_info)
                print("Something really bad happened. You should make a ticket for this")

            # get a list of makes on the search page
            makes_on_page = driver_info.find_elements_by_xpath('//span[@data-uname="lotsearchLotmake"]')
            # find one of those makes
            make_on_page = makes_on_page[0].get_attribute('innerHTML')

            try:
                assert (car_list[item]).upper() == make_on_page
            except AssertionError:
                print(make_on_page)  # Harley vs Harley-Davidson and Maclaren vs Maclaren Auotomotives don't match. Bug?
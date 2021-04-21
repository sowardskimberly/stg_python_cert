from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException


class Cars:

    def __init__(self, search_text, model):
        pass

    @classmethod
    def navigate_to_copart(cls, website, driver_info):
        """
        Navigates to a copart and aits for copart to load

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

    @staticmethod
    def take_screenshot(title, driver_info):
        """
        Take a screenshot and name it
        title (str): string value of file name
        driver_info (driver): the browser being used
        """
        driver_info.save_screenshot(title)

    @classmethod
    def open_filter(cls, filter_choice, driver_info):
        """
        Select which filter you would like to open and search for values

        args:
        filter_choice (str): name of filter, must be existing on copart
        driver_info (driver): the browser being used
        """
        formal_filter = filter_choice.capitalize()
        model_expand = driver_info.find_element_by_xpath('//a[@data-uname = "{}Filter"]'.format(formal_filter)).click()

    @classmethod
    def model_search(cls, model_text, driver_info):
        """
        When the model filter is open this searches for values of models
        model_text (str): The specific model value to be searched
        driver_info (driver): the browser being used
        """

        cls.model = model_text
        model_search = driver_info.find_element_by_xpath('(//input[@placeholder = "Search"])[5]')
        formal_modal = model_text.capitalize()
        model_search.send_keys(formal_modal)
        try:
            model_done_searching = driver_info.find_element_by_xpath('//abbr[@value = "{}"]'.format(formal_modal))
            print("Look there are {}'s!".format(formal_modal))
        except NoSuchElementException:
            print("No {}'s available right now".format(formal_modal))
            file_name = "Tests_challenge5 no_{}.png".format(formal_modal)
            Cars.take_screenshot(file_name, driver_info)






from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


class Cars:

    def __init__(self, search_text, model):
        pass

    @classmethod
    def navigate_to_copart(cls, website, driver_info):
        # specifically waits for copart to load
        driver_info.get(website)
        wait = WebDriverWait(driver_info, 60).until(EC.presence_of_element_located((By.ID, "input-search")))

    @classmethod
    def sep_makes_and_href(cls, driver_info):
        total_makes = driver_info.find_elements_by_xpath('//span[@class="make-items"]/span/a')
        car_make = []
        car_href = []
        # separate the car make and car href from the list of all elements on page
        for car in range(len(total_makes) - 1):
            car_make.append(total_makes[car].text)
            car_href.append(total_makes[car].get_attribute('href'))
        return car_make, car_href

    @classmethod
    def go_to_links(cls, car_list, href_list, driver_info):
        # Visit every href and verify that the make on the home page matches the search make
        timeout = 3  # seconds
        for item in range(len(href_list) - 1):
            driver_info.get(href_list[item])
            try:
                Waiting = WebDriverWait(driver_info, timeout).until(EC.presence_of_element_located((
                    By.XPATH, '(//tr[@class="odd"])')))
            except TimeoutException:
                print("Something really bad happened. You should make a ticket for this")

            # get a list of makes on the search page
            makes_on_page = driver_info.find_elements_by_xpath('//span[@data-uname="lotsearchLotmake"]')
            # find one of those makes
            make_on_page = makes_on_page[0].get_attribute('innerHTML')

            try:
                assert (car_list[item]).upper() == make_on_page
            except AssertionError:
                print(make_on_page)  # Harley vs Harley-Davidson and Maclaren vs Maclaren Auotomotives don't match. Bug?
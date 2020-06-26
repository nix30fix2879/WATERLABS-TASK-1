# -----------------------------------------------------------
# Demonstrates how to sort jab code on web page using selenium ActionChains
#
# Email saxena.k989@gmail.com
# -----------------------------------------------------------
import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


class JabCodeOrdering:
    def __init__(self):
        # Given jab code order
        self.jab_code_order = ['J92.9', 'A10.2', 'E24.9', 'B10.2', 'F19.10', 'D10.11']

        # instantiate driver
        self.driver = webdriver.Chrome('C:\\chrome\\chromedriver.exe')

        # URL
        self.url = 'C:\\chrome\\index.html'

    def setupDriver(self):
        # Maximize browser window
        self.driver.maximize_window()
        # html file where jab codes are present
        self.driver.get(self.url)

    # get the list of all jab code present in  web page
    def get_current_element_order(self):
        array_of_elements = self.driver.find_elements_by_xpath("//tbody//tr")
        return array_of_elements

    # Arrange jab code on given sorted order based on x,y offset
    def arrangeJabCodes(self):
        for item in range(len(self.jab_code_order)):
            # retrieve jab code from webpage
            row = self.driver.find_element_by_xpath(
                "//tr[@class='ui-sortable-handle']//td[text()='" + self.jab_code_order[item] + "']")
            # find source element from given jab code list
            source_element = self.driver.find_element_by_xpath(
                "//tr[@class='ui-sortable-handle']//td[text()='" + self.jab_code_order[item] + "']")
            # get current order of elements
            current_order_of_elements = self.get_current_element_order()
            dest_element = current_order_of_elements[item]
            # Drag source elements to destination using negative offsets
            if dest_element.location['y'] - source_element.location['y'] < 0:
                ActionChains(self.driver).drag_and_drop_by_offset(source_element,
                                                                  0,
                                                                  dest_element.location['y'] -
                                                                  source_element.location[
                                                                      'y'] - 5).perform()
            else:
                # Drag source elements to destination using offsets
                ActionChains(self.driver).drag_and_drop_by_offset(source_element,
                                                                  0,
                                                                  dest_element.location['y'] -
                                                                  source_element.location[
                                                                      'y']).perform()
            time.sleep(2)

    # Terminate driver instance
    def terminateDriver(self):
        self.driver.close()
        self.driver.quit()


if __name__ == '__main__':
    instance = JabCodeOrdering()
    instance.setupDriver()
    instance.arrangeJabCodes()
    instance.terminateDriver()

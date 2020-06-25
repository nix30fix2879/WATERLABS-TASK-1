# -----------------------------------------------------------
# demonstrates how to sort jab code on web page using selenium ActionChains
#
# email saxena.k989@gmail.com
# -----------------------------------------------------------
import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

# Given jab code order
jab_code_order = ['J92.9', 'A10.2', 'E24.9', 'B10.2', 'F19.10', 'D10.11']

# instantiate driver
driver = webdriver.Chrome('C:\\chrome\\chromedriver.exe')


class JabCodeOrdering:

    def setupDriver(self):
        # Maximize browser window
        driver.maximize_window()
        # html file where jab codes are present
        driver.get("C:\\chrome\\index.html")

    # get the list of all jab code present in  web page
    def get_current_element_order(self):
        array_of_elements = driver.find_elements_by_xpath("//tbody//tr")
        return array_of_elements

    # Arrange jab code on given sorted order based on x,y offset
    def arrangeJabCodes(self):
        for item in range(len(jab_code_order)):
            row = driver.find_element_by_xpath(
                "//tr[@class='ui-sortable-handle']//td[text()='" + jab_code_order[item] + "']")
            print(row.text)
            source_element = driver.find_element_by_xpath(
                "//tr[@class='ui-sortable-handle']//td[text()='" + jab_code_order[item] + "']")
            current_order_of_elements = self.get_current_element_order()
            dest_element = current_order_of_elements[item]
            if dest_element.location['y'] - source_element.location['y'] < 0:
                ActionChains(driver).drag_and_drop_by_offset(source_element,
                                                             0,
                                                             dest_element.location['y'] -
                                                             source_element.location[
                                                                 'y'] - 5).perform()
            else:
                ActionChains(driver).drag_and_drop_by_offset(source_element,
                                                             0,
                                                             dest_element.location['y'] -
                                                             source_element.location[
                                                                 'y']).perform()
            time.sleep(2)

    def terminateDriver(self):
        driver.close()
        driver.quit()


if __name__ == '__main__':
    instance = JabCodeOrdering()
    instance.setupDriver()
    instance.arrangeJabCodes()
    instance.terminateDriver()

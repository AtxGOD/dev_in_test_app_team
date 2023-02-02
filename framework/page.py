import logging

from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from account import account


class Page:
    valid_login = account['username']
    valid_password = account['password']

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 12)

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def write_text(self, element, text):
        element.send_keys(text)

    def click_element(self, element):
        return element.click()

    def click_back(self):
        self.driver.back()

    def is_element_exists(self, locator):
        try:
            elem = self.find_element(locator).get_attribute('text')
            logging.info("element exists")
            return elem
        except NoSuchElementException:
            logging.info("element doesn't exists")
            return False

    def wait_element(self, locator):
        try:
            return self.wait.until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            return False




import logging

from selenium.webdriver.common.by import By

from .login_page import LoginPage


class SideBarLocators:
    LOCATOR_SIDE_BAR_BUTTON = (By.XPATH, '//*[@resource-id="com.ajaxsystems:id/menuDrawer" and @index=2]')
    LOCATOR_ADD_HUB_BUTTON = (By.ID, 'com.ajaxsystems:id/addHub')
    LOCATOR_APP_SETTINGS_BUTTON = (By.ID, 'com.ajaxsystems:id/settings')
    LOCATOR_HELP_BUTTON = (By.ID, 'com.ajaxsystems:id/help')
    LOCATOR_PERORT_A_PROBLEM_BUTTON = (By.ID, 'com.ajaxsystems:id/logs')
    LOCATOR_VIDEO_SURVEILLANCE_BUTTON = (By.ID, 'com.ajaxsystems:id/camera')


class SideBarPage(LoginPage):
    def log_in(self):
        self.click_on_log_in_button()
        self.enter_username_and_password(self.valid_login, self.valid_password)
        self.click_log_in_next_button()

        self.wait_element(SideBarLocators.LOCATOR_SIDE_BAR_BUTTON)
        elem = self.find_element(SideBarLocators.LOCATOR_SIDE_BAR_BUTTON)
        self.click_element(elem)
        logging.info('logged in')

    def click_side_bar_elements(self, element):
        side_bar = self.find_element(SideBarLocators.LOCATOR_SIDE_BAR_BUTTON)
        logging.info(f'clicked {side_bar.get_attribute("text")}')
        self.click_element(side_bar)

        elem = self.find_element(element)
        self.click_element(elem)

    def try_to_find_element(self, xpath):
        return self.is_element_exists((By.XPATH, xpath))




import logging

from selenium.webdriver.common.by import By

from .page import Page


class LoginPageLocators:
    LOCATOR_LOG_IN_BUTTON = (By.ID, 'com.ajaxsystems:id/login')
    LOCATOR_CREATE_ACCOUNT_BUTTON = (By.ID, 'com.ajaxsystems:id/registration')
    LOCATOR_LOG_IN_TEXT_FIELD = (By.ID, 'com.ajaxsystems:id/login')
    LOCATOR_PASSWORD_TEXT_FIELD = (By.ID, 'com.ajaxsystems:id/password')
    LOCATOR_LOG_IN_NEXT_BUTTON = (By.ID, 'com.ajaxsystems:id/next')
    LOCATOR_ADD_HUB_BUTTON = (By.ID, 'com.ajaxsystems:id/text')
    LOCATOR_SNACK_BAR_TEXT = (By.ID, 'com.ajaxsystems:id/snackbar_text')


class LoginPage(Page):

    def click_on_log_in_button(self):
        element = self.find_element(LoginPageLocators.LOCATOR_LOG_IN_BUTTON)
        self.click_element(element)
        logging.debug('clicked on log in button')

    def enter_username_and_password(self, login, password):
        self.wait_element(LoginPageLocators.LOCATOR_LOG_IN_TEXT_FIELD)
        log_in_element = self.find_element(LoginPageLocators.LOCATOR_LOG_IN_TEXT_FIELD)
        self.click_element(log_in_element)
        self.write_text(log_in_element, login)
        logging.debug('entered login')

        password_element = self.find_element(LoginPageLocators.LOCATOR_PASSWORD_TEXT_FIELD)
        self.click_element(password_element)
        self.write_text(password_element, password)
        logging.debug('entered password')

    def click_log_in_next_button(self):
        element = self.find_element(LoginPageLocators.LOCATOR_LOG_IN_NEXT_BUTTON)
        self.click_element(element)
        logging.debug('clicked log in')

    def check_logged_in(self):
        self.wait_element(LoginPageLocators.LOCATOR_ADD_HUB_BUTTON)
        return self.is_element_exists(LoginPageLocators.LOCATOR_ADD_HUB_BUTTON)

    def check_wrong_field(self):
        self.wait_element(LoginPageLocators.LOCATOR_SNACK_BAR_TEXT)
        return self.is_element_exists(LoginPageLocators.LOCATOR_SNACK_BAR_TEXT)



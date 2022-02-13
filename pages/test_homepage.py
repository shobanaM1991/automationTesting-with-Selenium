
from Locators.test_locators import Locators
import os
import sys


class HomePage():

    def __init__(self, driver):
        self.driver = driver

        self.welcome_link_id = Locators.welcome_link_id
        self.logout_link_linktext = Locators.logout_link_linktext

    def click_welcome(self):
        self.driver.find_element_by_id(self.welcome_link_id).click()

    def click_onLogout(self):
        self.driver.find_element_by_link_text(
            self.logout_link_linktext).click()

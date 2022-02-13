from Locators.test_locators import Locators
import os
import sys


class LoginPage():

    def __init__(self, driver):
        self.driver = driver

        self.username_textbox_id = Locators.username_textbox_id
        self.password_textbox_id = Locators.password_textbox_id
        self.loginbutton_id = Locators.loginbutton_id
        #self.invalidUsername_message_xpath = Locators.invalidusername_xpath
        self.invalidUsernameId = Locators.invalidusername_id

    def enter_username(self, username):
        self.driver.find_element_by_id(self.username_textbox_id).clear()
        self.driver.find_element_by_id(
            self.username_textbox_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element_by_id(self.password_textbox_id).clear()
        self.driver.find_element_by_id(
            self.password_textbox_id).send_keys(password)

    def click_loginbutton(self):
        self.driver.find_element_by_id(self.loginbutton_id).click()

    def check_invalid_username(self):
        #msg = self.driver.find_element_by_xpath(self.invalidUsername_message_xpath).text
        msg = self.driver.find_element_by_id(self.invalidUsernameId).text
        return msg

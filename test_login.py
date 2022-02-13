
import os
import time
import HtmlTestRunner
import unittest
import sys

import selenium


from Pages.test_homepage import *
from Pages.test_loginpage import *

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class LoginTest(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome(
            executable_path=r'C:\Users\dhine\Desktop\chromedriver')
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_01_login_valid(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")

        loginobj = LoginPage(driver)
        loginobj.enter_username("Admin")
        loginobj.enter_password("admin123")
        loginobj.click_loginbutton()

        homeObj = HomePage(driver)
        homeObj.click_welcome()
        homeObj.click_onLogout()

        time.sleep(2)

    def test_02_login_valid(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")

        loginobj = LoginPage(driver)
        loginobj.enter_username("Admin1")
        loginobj.enter_password("admin123")
        loginobj.click_loginbutton()
        message = loginobj.check_invalid_username()
        self.assertEqual(message, "Invalid credentials")

        time.sleep(2)

    @classmethod
    def tearDown(cls):
        cls.driver.save_screenshot('screenshot.png')
        cls.driver.close()
        print("Completed")


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output=r'D:\Shobana\Projects\git-py-projects\OrangeORM\Rport'))

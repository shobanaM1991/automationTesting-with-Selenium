import os, sys
sys.path.insert(1, r'E:\MachineLearning\selenium_automation_tests\testcase_unittest\POM_ProjectDemo\pages')
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time
import HtmlTestRunner

from test_loginpage import LoginPage
from test_homepage import HomePage


class LoginTest(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome(executable_path= r'C:\Users\Dhinesh\Desktop\chromedriver_win32\chromedriver')
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
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output = r'E:\MachineLearning\selenium_automation_tests\testcase_unittest\POM_ProjectDemo\Rport'))

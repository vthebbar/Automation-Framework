import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import sys

from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_Login:   # Specify test case ID here in class name

    baseURL = ReadConfig.getAppURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getUserPassword()

    logger = LogGen.log_gen()     # class name. method name,  it will return logger object

    def test_homePageTitle(self, setup):
        self.logger.info("***********Test_001_Login**********")
        self.logger.info("***********Verify Home Page Title**********")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title

        if act_title == "Your store. Login":
            self.driver.close()
            self.logger.info("***********Verify Home Page Title - PASSED **********")
            assert True

        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homePageTitle.png")
            self.driver.close()
            self.logger.error("***********Verify Home Page Title - FAILED **********")
            assert False

    def test_login(self, setup):
        self.logger.info("***********Verify Login Page Title**********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title

        if act_title == "Dashboard / nopCommerce administration":
            self.driver.close()
            self.logger.info("***********Verify Login Page Title - PASSED **********")
            assert True

        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_login.png")
            self.driver.close()
            self.logger.error("***********Verify Login Page Title - FAILED **********")
            assert False


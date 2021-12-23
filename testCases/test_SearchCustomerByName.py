import time

import pytest
from selenium import webdriver
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from pageObjects.SearchCustomerPage import SearchCustomer
from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomerPage import AddCustomer

class Test_012_SearchCustomerByName:

    base_url = ReadConfig.getAppURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getUserPassword()

    logger = LogGen.log_gen()

    @pytest.mark.sanity
    def test_search_customer_by_name(self,setup):

        self.logger.info("******** Starting Test_012_SearchCustomerByName ******** ")
        self.driver = setup
        self.driver.get(self.base_url)

        self.logger.info("******* Starting Login **********")
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("********* Login Successful ****************")

        self.logger.info("***** Navigating to customer search page ************")
        self.addCust = AddCustomer(self.driver)
        self.addCust.click_on_customes_menu()
        self.addCust.click_on_customers_submenu()
        self.logger.info("********* Search page displayed ***********")

        self.logger.info("****** starting search ************")
        self.search = SearchCustomer(self.driver)
        self.search.set_first_name("John")
        self.search.set_last_name("Smith")
        self.search.click_search()
        time.sleep(2)
        flag = self.search.search_customer_by_name("John Smith")
        self.logger.info("********** Search completed **********")

        if flag == "Found":
            self.logger.info("********* Search element found ***********")
            self.driver.save_screenshot(".\\Screenshots\\Test_012_SearchCustomerByName_Pass.png")
            assert True
            self.driver.close()
        else:
            self.logger.info("********** Search element NOT found************")
            self.driver.save_screenshot(".\\Screenshots\\Test_012_SearchCustomerByName_Fail.png")
            self.driver.close()
            assert False

        self.logger.info("****** Completed Test_012_SearchCustomerByName *********** ")

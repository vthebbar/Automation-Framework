import time

import pytest
from selenium import webdriver
from utilities.readProperties import ReadConfig
from pageObjects.SearchCustomerPage import SearchCustomer
from pageObjects.LoginPage import LoginPage
from utilities.customLogger import LogGen
from pageObjects.AddCustomerPage import AddCustomer

class Test_011_SearchCustomerByEmail:

    base_url= ReadConfig.getAppURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getUserPassword()

    logger = LogGen.log_gen()

    @pytest.mark.regression
    def test_search_customer_by_email(self,setup):
        self.logger.info("**********Starting Test_011_SearchCustomerByEmail*********")
        self.driver = setup
        self.driver.get(self.base_url)

        self.logger.info("************Starting Login**********************")
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************Login Successful*******************")

        self.logger.info("**************Navigating to Customer Search Page****")
        self.addCust = AddCustomer(self.driver)
        self.addCust.click_on_customes_menu()
        time.sleep(1)
        self.addCust.click_on_customers_submenu()
        self.logger.info("********Customer search page displayed***************")

        self.logger.info("***********Starting Search******************")
        self.search = SearchCustomer(self.driver)

        self.search.set_email("admin@yourStore.com")
        self.search.click_search()
        time.sleep(4)
        self.logger.info("***************Search Completed**********")

        self.flag = self.search.search_customer_by_email("admin@yourStore.com")

        if self.flag == "Found":
            self.driver.save_screenshot(".\\Screenshots\\Test_011_SearchCustomerByEmail_pass.png")
            assert True
            self.logger.info("***********Search Element Found**********")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\Test_011_SearchCustomerByEmail_Fail.png")
            self.logger.info("***************Search Element Not found********")
            self.driver.close()
            assert False

        self.logger.info("*************Completed Test_011_SearchCustomerByEmail*******************")
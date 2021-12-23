import time

import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from webdriver_manager.chrome import ChromeDriverManager
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import ExcelUtility

class Test_002_DDT_Login:   # Specify test case ID here in class name

    baseURL = ReadConfig.getAppURL()
    path = ".//TestData/TestData.xlsx"

    logger = LogGen.log_gen()

    @pytest.mark.functional
    def test_login_ddt(self, setup):
        self.logger.info("***********Test_002_DDT_Login**********")
        self.logger.info("***********Verifying Login DDT **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)


        self.rows = ExcelUtility.getRowCount(self.path,"Sheet1")
        print("Number of rows=", self.rows)

        list_status=[] # empty list

        for r in range(2,self.rows+1):
            self.user = ExcelUtility.readExcel(self.path,"Sheet1",r,1)
            self.password = ExcelUtility.readExcel(self.path,"Sheet1",r,2)
            self.expected = ExcelUtility.readExcel(self.path,"Sheet1",r,3)

            print("ID=",self.user)
            print("Password=", self.password)

            self.lp.setUserName(self.user)
            time.sleep(2)
            self.lp.setPassword(self.password)
            time.sleep(2)
            self.lp.clickLogin()
            time.sleep(2)

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.expected == "Pass":
                    self.logger.info("Test Passed")
                    self.lp.clickLogout()
                    time.sleep(2)
                    list_status.append("Pass")
                elif self.expected == "Fail":
                    self.logger.info("Test Failed")
                    self.lp.clickLogout()
                    time.sleep(2)
                    list_status.append("Fail")

            elif act_title != exp_title:
                if self.expected == "Pass":
                    self.logger.info("Test Failed")
                    list_status.append("Fail")
                elif self.expected == "Fail":
                    self.logger.info("Test Passed")
                    list_status.append("Pass")

        if "Fail" not in list_status:
            self.logger.info("***********Login DDT Passed**************")
            self.driver.close()
            assert True
        else:
            self.logger.info("************Login DDT Failed*************")
            self.driver.close()
            assert False

        self.logger.info("*****End of Test_002_DDT************* ")
        self.logger.info("*****Test_002_DDT_Login Completed********* ")

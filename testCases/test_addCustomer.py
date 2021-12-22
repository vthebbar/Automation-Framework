import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from pageObjects.AddCustomerPage import AddCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from pageObjects.LoginPage import LoginPage
from utilities.randomEmailGenerator import RandomEmail

class Test_010_AddCustomer:

    base_url = ReadConfig.getAppURL()
    user_id = ReadConfig.getUserEmail()
    password = ReadConfig.getUserPassword()

    logger = LogGen.log_gen() # Logger to generate log

    def test_AddCustomer(self, setup):
        self.logger.info("********Starting Test_010_AddCustomer **********")
        self.driver = setup

        self.driver.get(self.base_url)

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.user_id)
        time.sleep(2)
        self.lp.setPassword(self.password)
        time.sleep(2)
        self.lp.clickLogin()

        self.logger.info("***********Login Completed******************")

        self.logger.info("***********Starting Add Customer ***************")

        self.addCustomer = AddCustomer(self.driver)
        self.addCustomer.click_on_customes_menu()
        time.sleep(1)
        self.addCustomer.click_on_customers_submenu()

        self.addCustomer.click_on_add_new_button()

        self.email = RandomEmail.random_email(8) # To generate random email id

        self.addCustomer.set_email(self.email)  # Need to generate random email id, as this should be unique
        self.addCustomer.set_password("abc@123")
        self.addCustomer.set_first_name("Raj")
        self.addCustomer.set_last_name("Kumar")
        self.addCustomer.set_gender("Male")
        self.addCustomer.set_date_of_birth("12/12/2010")
        self.addCustomer.set_company_name("XYZ")
        self.addCustomer.set_is_tax_exempt("Yes")

        # scroll down
        self.ele = self.driver.find_element(By.ID, AddCustomer.txt_AdminComment_id)
        self.driver.execute_script("arguments[0].scrollIntoView();", self.ele)
        #action = ActionChains(self.driver)
        #action.move_to_element(self.ele).perform()

        news_list = self.driver.find_elements(By.XPATH,"//select[@id='SelectedNewsletterSubscriptionStoreIds']/option")

        self.addCustomer.set_news_letter(news_list,['Your store name','Test store 2'])



        self.elements = self.driver.find_elements(By.XPATH, "//select[@id='SelectedCustomerRoleIds']/option")

        self.addCustomer.set_customer_roles(self.elements,['Forum Moderators','Salesman'])
        self.addCustomer.set_manager_of_vendor("Vendor 2")
        self.addCustomer.set_active("Yes")
        self.addCustomer.set_admin_comment("Admin comment details")

        self.addCustomer.click_save()
        time.sleep(2)

        message_element = self.driver.find_element(By.XPATH,"//div[@class='alert alert-success alert-dismissable']")
        message_text = message_element.text
        print(message_text)
        if "The new customer has been added successfully" in message_text:

            self.logger.info("*********** Add Customer Successful ***************")
            self.driver.save_screenshot(".\\Screenshots\\Test_010_AddCustomer_Pass.png")
            assert True
            self.driver.close()

        else:
            self.driver.save_screenshot(".\\Screenshots\\Test_010_AddCustomer_Failed.png")
            self.driver.close()
            self.logger.info("***********Add Customer failed ***************")
            assert False

        self.logger.info("********Completed Test_010_AddCustomer **********")
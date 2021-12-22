from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Add customer page
class AddCustomer:

    lnk_CustomersMainMenu_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    lnk_CustomersSubMenu_xpath = "//a[@href='/Admin/Customer/List']//p[contains(text(),' Customers')]"
    btn_AddNew_xpath = "//a[@href='/Admin/Customer/Create']"

    # Form elements
    txt_Email_id = "Email"
    txt_Password_id = "Password"
    txt_FirstName_id ="FirstName"
    txt_LastName_id = "LastName"
    rdbtn_GenderMale_id = "Gender_Male"
    rdbtn_GenderFemale_id = "Gender_Female"
    txt_DateOfBirth_id = "DateOfBirth"
    txt_Company_id = "Company"
    chkbox_IsTaxExempt_id = "IsTaxExempt"

    txt_Newsletter_xpath = "//div[@class='k-multiselect-wrap k-floatwrap']"
    #"//input[@class='k-input k-readonly']"
    #new letter values-start
    #lstItem_YouStoreName_xpath = "//li[text()='Your store name']"
    #lstItem_Teststore2_xpath = "//li[text()='Test store 2']"
    # new letter values-end

    txt_CustomerRoles_xpath = "//ul[@id='SelectedCustomerRoleIds_taglist']"
    # Elements within customer roles -start
    remove_Registered_xpath = "//ul[@id='SelectedCustomerRoleIds_taglist']/li/span[2]" # X button remove item from list
    lstItem_Registered_xpath  = "//span[text()='Registered']"
    lstItem_Administrators_xpath = "//span[text()='Administrators']"
    lstItem_ForumModerators_xpath = "//span[text()='Forum Moderators']"
    lstItem_Guests_xpath = "//span[text()='Guests']"
    lstItem_Vendors_xpath = "//span[text()='Vendors']"
    # Elements within customer roles -End

    drpdown_ManagerOfVendor_id = "VendorId"
    chkbox_Active_id = "Active"
    txt_AdminComment_id = "AdminComment"
    btn_Save_name = "save"

    # constructor to initialize driver
    def __init__(self, driver):
        self.driver = driver


    def click_on_customes_menu(self):
        self.driver.find_element(By.XPATH,self.lnk_CustomersMainMenu_xpath).click()

        #ele = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,self.lnk_CustomersMainMenu_xpath)))
        #ele.click()

    def click_on_customers_submenu(self):
        self.driver.find_element(By.XPATH, self.lnk_CustomersSubMenu_xpath).click()

    def click_on_add_new_button(self):
        self.driver.find_element(By.XPATH, self.btn_AddNew_xpath).click()

    def set_email(self,email):
        self.driver.find_element(By.ID, self.txt_Email_id).clear()
        self.driver.find_element(By.ID, self.txt_Email_id).send_keys(email)

    def set_password(self,password):
        self.driver.find_element(By.ID, self.txt_Password_id).clear()
        self.driver.find_element(By.ID, self.txt_Password_id).send_keys(password)

    def set_first_name(self,firstName):
        self.driver.find_element(By.ID, self.txt_FirstName_id).clear()
        self.driver.find_element(By.ID, self.txt_FirstName_id).send_keys(firstName)

    def set_last_name(self,lastName):
        self.driver.find_element(By.ID,self.txt_LastName_id).clear()
        self.driver.find_element(By.ID, self.txt_LastName_id).send_keys(lastName)

    def set_gender(self, gender):
        if gender == "Male":
            self.driver.find_element(By.ID, self.rdbtn_GenderMale_id).click()
        elif gender == "Female":
            self.driver.find_element(By.ID, self.rdbtn_GenderFemale_id).click()
        else:
            self.driver.find_element(By.ID, self.rdbtn_GenderMale_id).click()

    def set_date_of_birth(self, dob):
        self.driver.find_element(By.ID,self.txt_DateOfBirth_id).clear()
        self.driver.find_element(By.ID,self.txt_DateOfBirth_id).send_keys(dob)

    def set_company_name(self, compName):
        self.driver.find_element(By.ID,self.txt_Company_id).clear()
        self.driver.find_element(By.ID, self.txt_Company_id).send_keys(compName)

    def set_is_tax_exempt(self,taxFlag):
        if taxFlag == "Yes":
            self.driver.find_element(By.ID, self.chkbox_IsTaxExempt_id).click()
        else:
            pass

    # Function is able to select multiple value for Newsletter field
    def set_news_letter(self, news_letter_list, select_news):
        time.sleep(1)
        for n in news_letter_list:
            ele = n.get_attribute('text')
            print("Element=", ele)
            for s in select_news:
                if ele == s:
                    self.driver.find_element(By.XPATH,"//*[@id='customer-info']/div[2]/div[9]/div[2]/div/div[1]/div/div").click()
                    time.sleep(2)
                    self.news_list_item = self.driver.find_element(By.XPATH,"//li[text()='"+s+"']").click()
                    time.sleep(2)
                    break
                #self.driver.execute_script("arguments[0].click();", self.news_list_item)

    # if need to select multiple roles, can pass multiple values

    def set_customer_roles(self, elements_list, values_to_select):

        if len(values_to_select) == 1 and values_to_select[0] == "Registered":
            pass
        else:
            for e in elements_list:
                e_text_value = e.get_attribute('text')
                for v in values_to_select:
                    if e_text_value == v:
                        if v == "Guest":
                            time.sleep(2)
                            self.driver.find_element(By.XPATH, self.remove_Registered_xpath).click()
                        if v == "Registered":
                            break
                        self.driver.find_element(By.XPATH,
                                            "//*[@id='customer-info']/div[2]/div[10]/div[2]/div/div[1]/div/div").click()
                        time.sleep(2)
                        self.driver.find_element(By.XPATH, "//li[text()='" + v + "']").click()
                        time.sleep(2)
                        break

    def set_manager_of_vendor(self, value):
        drop_down_element = self.driver.find_element(By.ID,self.drpdown_ManagerOfVendor_id)
        select = Select(drop_down_element)
        select.select_by_visible_text(value)

    def set_active(self,active_flag):
        if active_flag == "No":
            self.driver.find_element(By.ID, self.chkbox_Active_id).click()
        else:
            pass

    def set_admin_comment(self,comment):
        self.driver.find_element(By.ID, self.txt_AdminComment_id).clear()
        self.driver.find_element(By.ID, self.txt_AdminComment_id).send_keys(comment)

    def click_save(self):
        self.driver.find_element(By.NAME, self.btn_Save_name).click()






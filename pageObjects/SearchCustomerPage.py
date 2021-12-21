# search customer
from selenium import webdriver
from selenium.webdriver.common.by import By

class SearchCustomer:

    txt_emailid_id = "SearchEmail"
    txt_firstname_id = "SearchFirstName"
    txt_lastname_id = "SearchLastName"
    btn_search_id = "search-customers"

    # ***********search result elements*****************
    search_results_xpath = "//table[@role='grid']"
    result_data_table_xpath = "//table[@id='customers-grid']"
    result_table_rows = "//table[@id='customers-grid']//tbody/tr"
    result_table_columns = "//table[@id='customers-grid']//tbody/tr/td"

    def __init__(self, driver):
        self.driver = driver


    def set_email(self, email):
        self.driver.find_element(By.ID, self.txt_emailid_id).clear()
        self.driver.find_element(By.ID, self.txt_emailid_id).send_keys(email)

    def set_first_name(self,fname):
        self.driver.find_element(By.ID, self.txt_firstname_id).clear()
        self.driver.find_element(By.ID, self.txt_firstname_id).send_keys(fname)

    def set_last_name(self, lname):
        self.driver.find_element(By.ID, self.txt_lastname_id).clear()
        self.driver.find_element(By.ID, self.txt_lastname_id).send_keys(lname)

    def click_search(self):
        self.driver.find_element(By.ID, self.btn_search_id).click()

    def get_no_of_rows(self):
        rows = self.driver.find_elements(By.XPATH, self.result_table_rows)
        return len(rows)

    def get_no_of_columns(self):
        col = self.driver.find_elements(By.XPATH, self.result_table_columns)
        return len(col)

    def search_customer_by_email(self, email):
        flag = 0
        for r in range(1,self.get_no_of_rows()+1):  # 0 excluded , as it is table header
            table = self.driver.find_element(By.XPATH,self.search_results_xpath)
            emailid = table.find_element(By.XPATH,"//table[@id='customers-grid']//tbody/tr["+str(r)+"]/td[2]").text

            if emailid == email:
                flag = 1
                break
        return flag


    def search_customer_by_name(self, name):
        flag = 0
        for r in range(1,self.get_no_of_rows()+1):  # 0 excluded , as it is table header
            table = self.driver.find_element(By.XPATH,self.search_results_xpath)
            tbl_name = table.find_element(By.XPATH,"//table[@id='customers-grid']//tbody/tr["+str(r)+"]/td[3]").text

            if tbl_name == name:
                flag = 1
                break
        return flag


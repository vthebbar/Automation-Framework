# login page

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:

    textbox_username_id = "Email"
    textbox_password_id = "Password"
    button_login_xpath = "//button[@class='button-1 login-button']"
    link_logout_linktext = "Logout"

    # constructor to initialize driver

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self,username):
        #self.driver.find_element(By.ID, self.textbox_username_id).clear()
        #self.driver.find_element(By.ID, self.textbox_username_id).send_keys(username)
        login_id=WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.ID,self.textbox_username_id)))
        login_id.clear()
        login_id.send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.ID, self.textbox_password_id).clear()
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    def clickLogout(self):
        self.driver.find_element(By.LINK_TEXT, self.link_logout_linktext).click()







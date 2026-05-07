from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    USERNAME =(By.ID,"user-name")
    PASSWORD= (By.ID,"password")
    LOGIN_BUTTON= (By.ID,"login-button")
    PRODUCT_TITLE = (By.CLASS_NAME,"title")
    
    def __init__(self,driver):
        super().__init__(driver)
        # because LoginPage is inheriting from BasePage. So constructor of parent class
        #sould also run
        
    def login_site(self, username,password):
        self.driver.find_element(*self.USERNAME).send_keys(username)
        self.driver.find_element(*self.PASSWORD).send_keys(password)
        button=self.driver.find_element(*self.LOGIN_BUTTON)
        button.click()
    def is_inventory_page_displayed(self):
        return self.driver.find_element(*self.PRODUCT_TITLE).text == "Products"
        
    
    
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import time
class LoginPage(BasePage):
    USERNAME =(By.ID,"user-name")
    PASSWORD= (By.ID,"password")
    LOGIN_BUTTON= (By.ID,"login-button")
    PRODUCT_TITLE = (By.CLASS_NAME,"title")
    ERROT_MSG = (By.XPATH,"//div[@class='error-message-container error']")
    LOGOUT_LINK =(By.ID,"logout_sidebar_link")
    MENU_BUTTON = (By.ID,"react-burger-menu-btn")
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
        
    
    def is_error_displayed(self):
        return self.driver.find_element(*self.ERROT_MSG).is_displayed()
    def click_logout(self):
      
        self.driver.find_element(*self.MENU_BUTTON).click()
        time.sleep(15)
        return self.driver.find_element(*self.LOGOUT_LINK).click()
    def is_login_page_displayed(self):
        
        return "saucedemo.com" in self.driver.current_url
        
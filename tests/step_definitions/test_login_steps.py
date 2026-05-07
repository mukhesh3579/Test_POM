from pytest_bdd import scenarios
from pytest_bdd import given, when, then  

from pages.login_page import LoginPage

scenarios("../features/login.feature")

@given("user open login page")
def open_login(driver):
    # create LoginPage object
    login = LoginPage(driver)
    login.open_url()
    
@when("user enters valid credetials")
def valid_login(driver):
    login = LoginPage(driver)
    login.login_site("standard_user","secret_sauce")

@then("user should navigate to inventory page")
def login_page_verification(driver):
     page = LoginPage(driver)
     assert page.is_inventory_page_displayed()
          
@when("user enters invalid credentials") 
def enter_invalid_credentials(driver):
    page=LoginPage(driver)
    page.login_site("wronguser","wrongpassword")
    
@then("login error should display")
def verify_display_error(driver):
    page = LoginPage(driver)
    assert page.is_error_displayed()
    
@when("user clicks logout button")
def logout(driver):
    page= LoginPage(driver)
    page.click_logout()
    
@then("user should navigate to login page")
def vrify_login_page(driver):
    page = LoginPage(driver)
    assert page.is_login_page_displayed()
    
    
    
    

         
    
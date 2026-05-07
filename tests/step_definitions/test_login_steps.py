from pytest_bdd import scenarios
from pytest_bdd import given, when, then

from pages.login_page import LoginPage

scenarios("../features/login.feature")

@given("user open login page")
def open_login(driver):
    # create LoginPage object
    login = LoginPage(driver)
    login.open_url()
    
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
def invalid_login(driver):
    login = LoginPage(driver)
    login.login_site("invalid_user","invalid_password") 

then("login error should display")
def login_error_verification(driver):
    page = LoginPage(driver)
    assert page.is_login_error_displayed()

          
      
    
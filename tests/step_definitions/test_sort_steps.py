from pytest_bdd import scenarios
from pytest_bdd import given, when, then  
import time
from pages.login_page import LoginPage
from pages.inventory_page import Inventory_Page
scenarios("../features/sort.feature")

@given("user open login page")
def open_login(driver):
    # create LoginPage object
    login = LoginPage(driver)
    login.open_url()
    
@when("user enters valid credetials")
def valid_login(driver):
    login = LoginPage(driver)
    login.login_site("standard_user","secret_sauce")
    time.sleep(2)

# Sort by Name (A to Z)
@when('user selects "Name (A to Z)" from dropdown')
def sort_name_a_to_z(driver):
    inventory = Inventory_Page(driver)
    inventory.select_sort_option("Name (A to Z)")
    time.sleep(2)

@then('products should be sorted alphabetically from A to Z')
def verify_a_to_z_sort(driver):
    inventory = Inventory_Page(driver)
    product_names = inventory.get_product_names()
    assert product_names == sorted(product_names), "Products are not sorted A to Z"

# Sort by Name (Z to A)
@when('user selects "Name (Z to A)" from dropdown')
def sort_name_z_to_a(driver):
    inventory = Inventory_Page(driver)
    inventory.select_sort_option("Name (Z to A)")
    time.sleep(2)

@then('products should be sorted alphabetically from Z to A')
def verify_z_to_a_sort(driver):
    inventory = Inventory_Page(driver)
    product_names = inventory.get_product_names()
    assert product_names == sorted(product_names, reverse=True), "Products are not sorted Z to A"

# Sort by Price (Low to High)
@when('user selects "Price (low to high)" from dropdown')
def sort_price_low_to_high(driver):
    inventory = Inventory_Page(driver)
    inventory.select_sort_option("Price (low to high)")
    time.sleep(2)

@then('products should be sorted by price from lowest to highest')
def verify_price_low_to_high_sort(driver):
    inventory = Inventory_Page(driver)
    product_prices = inventory.get_product_prices()
    assert product_prices == sorted(product_prices), "Products are not sorted by price (low to high)"

# Sort by Price (High to Low)
@when('user selects "Price (high to low)" from dropdown')
def sort_price_high_to_low(driver):
    inventory = Inventory_Page(driver)
    inventory.select_sort_option("Price (high to low)")
    time.sleep(2)

@then('products should be sorted by price from highest to lowest')
def verify_price_high_to_low_sort(driver):
    inventory = Inventory_Page(driver)
    product_prices = inventory.get_product_prices()
    assert product_prices == sorted(product_prices, reverse=True), "Products are not sorted by price (high to low)"

# Verify products are visible
@then('all products should be visible')
def verify_products_visible(driver):
    inventory = Inventory_Page(driver)
    products = inventory.get_all_products()
    assert len(products) > 0, "No products are visible on the page"

# Verify sort dropdown
@then('sort dropdown should be visible on inventory page')
def verify_sort_dropdown_visible(driver):
    inventory = Inventory_Page(driver)
    assert inventory.is_sort_dropdown_visible(), "Sort dropdown is not visible"

@then('sort dropdown should contain all available options')
def verify_sort_options(driver):
    inventory = Inventory_Page(driver)
    expected_options = ["Name (A to Z)", "Name (Z to A)", "Price (low to high)", "Price (high to low)"]
    available_options = inventory.get_sort_options()
    for option in expected_options:
        assert option in available_options, f"Option '{option}' is not available in sort dropdown"

# Verify default sort order
@then('products should be displayed in default order')
def verify_default_sort(driver):
    inventory = Inventory_Page(driver)
    products = inventory.get_all_products()
    assert len(products) > 0, "No products are displayed"
    # Default order is typically by Name (A to Z) or by catalog order
    time.sleep(2)

    
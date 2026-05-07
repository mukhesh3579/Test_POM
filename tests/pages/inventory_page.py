
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage
import time

class Inventory_Page(BasePage):
    # Locators
    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")
    SORT_DROPDOWN_SELECT = (By.CSS_SELECTOR, "select.product_sort_container")
    PRODUCTS_CONTAINER = (By.CLASS_NAME, "inventory_container")
    PRODUCT_ITEMS = (By.CLASS_NAME, "inventory_item")
    PRODUCT_NAME = (By.CLASS_NAME, "inventory_item_name")
    PRODUCT_PRICE = (By.CLASS_NAME, "inventory_item_price")

    def __init__(self, driver):
        super().__init__(driver)

    def select_sort_option(self, visible_text):
        """Select a sort option from the dropdown by visible text"""
        dropdown = self.driver.find_element(*self.SORT_DROPDOWN_SELECT)
        select = Select(dropdown)
        select.select_by_visible_text(visible_text)
        time.sleep(1)

    def get_all_products(self):
        """Get all product elements from the inventory page"""
        products = self.driver.find_elements(*self.PRODUCT_ITEMS)
        return products

    def get_product_names(self):
        """Get list of all product names in current sort order"""
        product_names = []
        products = self.driver.find_elements(*self.PRODUCT_ITEMS)
        for product in products:
            name = product.find_element(*self.PRODUCT_NAME).text
            product_names.append(name)
        return product_names

    def get_product_prices(self):
        """Get list of all product prices in current sort order"""
        product_prices = []
        products = self.driver.find_elements(*self.PRODUCT_ITEMS)
        for product in products:
            price_text = product.find_element(*self.PRODUCT_PRICE).text
            # Remove '$' and convert to float for comparison
            price = float(price_text.replace('$', ''))
            product_prices.append(price)
        return product_prices

    def is_sort_dropdown_visible(self):
        """Check if the sort dropdown is visible on the page"""
        try:
            dropdown = self.driver.find_element(*self.SORT_DROPDOWN)
            return dropdown.is_displayed()
        except:
            return False

    def get_sort_options(self):
        """Get all available sort options from the dropdown"""
        dropdown = self.driver.find_element(*self.SORT_DROPDOWN_SELECT)
        select = Select(dropdown)
        options = select.options
        option_texts = [option.text for option in options]
        return option_texts

    
        
        
import pytest
from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="function")
def driver():
    service =Service(
       ChromeDriverManager().install()
    )
    
    driver= webdriver.Chrome(service=service)
    driver.implicitly_wait(1)
    yield driver
    driver.quit()
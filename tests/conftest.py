import pytest
from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service


@pytest.fixture(scope="function")
def driver(request):
    """
    Fixture to initialize Selenium WebDriver.
    Use with --browser flag to specify: chrome (default) or edge
    Example: pytest --browser=edge
    """
    browser = request.config.getoption("--browser", default="chrome").lower()
    
    if browser == "edge":
        driver = webdriver.Edge()
    elif browser == "chrome":  # Default to Chrome
        driver = webdriver.Chrome()
    elif browser == "firefox":
         driver = webdriver.Firefox()
    
    driver.implicitly_wait(1)
    yield driver
    driver.quit()


def pytest_addoption(parser):
    """Add custom command-line option for browser selection"""
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Specify browser: chrome, edge or firefox (default: chrome)"
    )
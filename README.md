# Test Automation Framework

This repository contains automated tests for the SauceDemo application using Page Object Model (POM) with pytest-bdd and Selenium WebDriver.

## Project Structure

```
tests/
├── conftest.py              # Pytest fixtures and configuration
├── features/               # BDD feature files
│   ├── login.feature       # Login scenarios
│   └── sort.feature        # Product sorting scenarios
├── pages/                  # Page Object Model classes
│   ├── base_page.py        # Base page class
│   ├── login_page.py       # Login page object
│   ├── inventory_page.py   # Inventory page object
│   ├── cart_page.py        # Cart page object
│   ├── checkout_page.py    # Checkout page object
│   └── ...
└── step_definitions/       # BDD step definitions
    ├── test_login_steps.py # Login step implementations
    └── test_sort_steps.py  # Sort step implementations
```

## Prerequisites

- Python 3.9+
- Google Chrome browser
- Git

## Local Setup

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd Test_POM
   ```

2. **Create virtual environment:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run tests:**
   ```bash
   # Run all tests
   pytest tests/

   # Run specific feature
   pytest tests/ -k "sort"

   # Run with verbose output
   pytest tests/ -v

   # Generate HTML report
   pytest tests/ --html=reports/test-report.html
   ```

## CI/CD

This project uses GitHub Actions for continuous integration. The workflow:

- Runs on every push and pull request to `main` and `develop` branches
- Sets up Python 3.9 environment
- Installs Google Chrome
- Installs Python dependencies
- Runs all tests in headless mode
- Generates and uploads test reports

### Workflow Triggers

- Push to `main` or `develop` branches
- Pull requests targeting `main` or `develop` branches

### Test Reports

Test results are automatically uploaded as artifacts and can be downloaded from the Actions tab.

## Writing Tests

### Adding New Features

1. Create a new `.feature` file in `tests/features/`
2. Write scenarios using Gherkin syntax
3. Create corresponding step definitions in `tests/step_definitions/`
4. Implement page object methods in appropriate page classes

### Example Feature File

```gherkin
Feature: Product Sorting Functionality

Scenario: Sort products by Name (A to Z)
    Given user open login page
    When user enters valid credentials
    And user selects "Name (A to Z)" from dropdown
    Then products should be sorted alphabetically from A to Z
```

### Example Step Definition

```python
from pytest_bdd import given, when, then
from pages.login_page import LoginPage
from pages.inventory_page import Inventory_Page

@given("user open login page")
def open_login(driver):
    login = LoginPage(driver)
    login.open_url()

@when("user enters valid credentials")
def valid_login(driver):
    login = LoginPage(driver)
    login.login_site("standard_user", "secret_sauce")
```

## Browser Configuration

Tests run in headless mode in CI. For local development, you can modify `conftest.py` to run with a visible browser by removing the headless options.

## Contributing

1. Create a feature branch
2. Write tests for new functionality
3. Ensure all tests pass locally
4. Create a pull request
5. Wait for CI to pass
# Import the pytest library to enable the use of fixtures
import pytest
# Import the Page class from Playwright for type hinting (better code completion)
from playwright.sync_api import Page
# Import our LoginPage class so we can initialize it in the fixture
from pages.login_page import LoginPage

# This decorator marks the function as a 'fixture'
# Fixtures are used to provide a fixed baseline upon which tests can reliably execute
@pytest.fixture
def login_page(page: Page):
    """
    This fixture initializes the LoginPage object.
    It takes the 'page' object (provided by playwright-pytest) 
    and passes it to our LoginPage class.
    Every test that uses 'login_page' as an argument will have access to this object.
    """
    # Create an instance of the LoginPage class using the current browser page
    return LoginPage(page)
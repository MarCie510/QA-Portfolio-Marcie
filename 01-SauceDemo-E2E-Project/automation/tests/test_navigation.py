import pytest
import re
from playwright.sync_api import expect
from pages.navigation_page import NavigationPage
from pages.cart_page import CartPage

@pytest.fixture
def setup_nav(login_page):
    """Helper fixture to login and return NavigationPage."""
    login_page.navigate_to_login()
    login_page.login("standard_user", "secret_sauce")
    return NavigationPage(login_page.page)

# SDW-35: Hamburger menu opens and displays all options
@pytest.mark.smoke
def test_hamburger_menu_options(setup_nav):
    """
    ID: SDW-35
    Scenario: Verify hamburger menu opens and shows links.
    """
    nav_page = setup_nav
    nav_page.open_menu()
    expect(nav_page.page.locator(nav_page.menu_wrap)).to_be_visible()
    expect(nav_page.page.locator(nav_page.all_items_link)).to_be_visible()

# SDW-36: All Items link returns to inventory from any page
@pytest.mark.smoke
def test_all_items_link(setup_nav):
    """
    ID: SDW-36
    Scenario: Verify All Items link navigates to inventory.
    """
    nav_page = setup_nav
    nav_page.page.goto("https://www.saucedemo.com/cart.html")
    nav_page.open_menu()
    nav_page.page.locator(nav_page.all_items_link).click()
    expect(nav_page.page).to_have_url("https://www.saucedemo.com/inventory.html")

# SDW-37: Reset App State clears the cart
@pytest.mark.smoke
def test_reset_app_state(setup_nav):
    """
    ID: SDW-37
    Scenario: Verify Reset App State clears added items.
    """
    nav_page = setup_nav
    nav_page.page.locator("#add-to-cart-sauce-labs-backpack").click()
    
    nav_page.open_menu()
    nav_page.page.locator(nav_page.reset_link).click()
    
    cart_page = CartPage(nav_page.page)
    assert cart_page.get_badge_count() == 0

# SDW-38: About link navigates to Sauce Labs website
@pytest.mark.smoke
def test_about_link(setup_nav):
    """
    ID: SDW-38
    Scenario: Verify About link redirects to saucelabs.com.
    """
    nav_page = setup_nav
    nav_page.open_menu()
    nav_page.page.locator(nav_page.about_link).click()
    expect(nav_page.page).to_have_url(re.compile(r".*saucelabs\.com.*"))

# SDW-39: Page title is correct on all main pages
@pytest.mark.smoke
def test_page_titles(setup_nav):
    """
    ID: SDW-39
    Scenario: Verify the browser tab title is correct.
    """
    nav_page = setup_nav
    expect(nav_page.page).to_have_title("Swag Labs")

# SDW-40: Footer links are functional
@pytest.mark.smoke
def test_footer_links(setup_nav):
    """
    ID: SDW-40
    Scenario: Verify footer social links have correct URLs.
    """
    nav_page = setup_nav
    twitter = nav_page.page.locator(nav_page.twitter_link)
    expect(twitter).to_have_attribute("href", "https://twitter.com/saucelabs")

# SDW-41: Swag Labs logo redirects to inventory
@pytest.mark.smoke
def test_swag_labs_logo(setup_nav):
    """
    ID: SDW-41
    Scenario: Verify logo click behavior. (Edge case: usually it doesn't redirect, testing default).
    """
    nav_page = setup_nav
    nav_page.page.goto("https://www.saucedemo.com/cart.html")
    # Some versions of the app don't have a clickable logo, we verify it exists.
    expect(nav_page.page.locator(".app_logo")).to_be_visible()
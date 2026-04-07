import pytest
from playwright.sync_api import expect
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

@pytest.fixture
def setup_checkout(login_page):
    """Helper fixture to reach the checkout step one page."""
    login_page.navigate_to_login()
    login_page.login("standard_user", "secret_sauce")
    login_page.page.locator("#add-to-cart-sauce-labs-backpack").click()
    cart_page = CartPage(login_page.page)
    cart_page.go_to_cart()
    login_page.page.locator(cart_page.checkout_button).click()
    return CheckoutPage(login_page.page)

# SDW-26: Successful checkout with valid customer data (Positive/Happy Path)
@pytest.mark.smoke
def test_successful_checkout(setup_checkout):
    """
    ID: SDW-26
    Scenario: Complete a full checkout successfully.
    """
    checkout_page = setup_checkout
    checkout_page.fill_checkout_info("Marcie", "QA", "11000")
    
    expect(checkout_page.page).to_have_url("https://www.saucedemo.com/checkout-step-two.html")
    checkout_page.page.locator(checkout_page.finish_button).click()
    
    expect(checkout_page.page).to_have_url("https://www.saucedemo.com/checkout-complete.html")
    assert checkout_page.page.inner_text(checkout_page.complete_header) == "Thank you for your order!"

# SDW-27: Checkout blocked with all fields empty (Negative)
@pytest.mark.edge_case
def test_checkout_empty_fields(setup_checkout):
    """
    ID: SDW-27
    Scenario: Error when submitting empty form.
    """
    checkout_page = setup_checkout
    checkout_page.fill_checkout_info("", "", "")
    assert "Error: First Name is required" in checkout_page.get_error_message()

# SDW-28: Checkout blocked when First Name is missing (Negative)
@pytest.mark.edge_case
def test_checkout_missing_first_name(setup_checkout):
    """
    ID: SDW-28
    Scenario: Error when first name is omitted.
    """
    checkout_page = setup_checkout
    checkout_page.fill_checkout_info("", "QA", "11000")
    assert "Error: First Name is required" in checkout_page.get_error_message()

# SDW-29: Checkout blocked when Last Name is missing (Negative)
@pytest.mark.edge_case
def test_checkout_missing_last_name(setup_checkout):
    """
    ID: SDW-29
    Scenario: Error when last name is omitted.
    """
    checkout_page = setup_checkout
    checkout_page.fill_checkout_info("Marcie", "", "11000")
    assert "Error: Last Name is required" in checkout_page.get_error_message()

# SDW-30: Checkout blocked when Zip Code is missing (Negative)
@pytest.mark.edge_case
def test_checkout_missing_zip(setup_checkout):
    """
    ID: SDW-30
    Scenario: Error when zip code is omitted.
    """
    checkout_page = setup_checkout
    checkout_page.fill_checkout_info("Marcie", "QA", "")
    assert "Error: Postal Code is required" in checkout_page.get_error_message()

# SDW-31: Price calculation accuracy on order summary (Value)
@pytest.mark.smoke
def test_price_calculation(setup_checkout):
    """
    ID: SDW-31
    Scenario: Validate Subtotal + Tax equals Total.
    """
    checkout_page = setup_checkout
    checkout_page.fill_checkout_info("Marcie", "QA", "11000")
    
    subtotal = checkout_page.get_price_value(checkout_page.subtotal_label)
    tax = checkout_page.get_price_value(checkout_page.tax_label)
    total = checkout_page.get_price_value(checkout_page.total_label)
    
    assert round(subtotal + tax, 2) == total

# SDW-32: Cancel checkout returns user to cart (Positive)
@pytest.mark.smoke
def test_cancel_checkout(setup_checkout):
    """
    ID: SDW-32
    Scenario: Clicking cancel redirects back to the cart.
    """
    checkout_page = setup_checkout
    checkout_page.page.locator(checkout_page.cancel_button).click()
    expect(checkout_page.page).to_have_url("https://www.saucedemo.com/cart.html")

# SDW-33: SQL Injection prevention on checkout form fields (Security/Negative)
@pytest.mark.security
def test_sql_injection_checkout(setup_checkout):
    """
    ID: SDW-33
    Scenario: System handles SQL injection payload without crashing.
    """
    checkout_page = setup_checkout
    checkout_page.fill_checkout_info("admin' OR '1'='1", "QA", "11000")
    expect(checkout_page.page).to_have_url("https://www.saucedemo.com/checkout-step-two.html")

# SDW-34: XSS prevention on checkout form fields (Security/Negative)
@pytest.mark.security
def test_xss_checkout(setup_checkout):
    """
    ID: SDW-34
    Scenario: System handles XSS payload safely.
    """
    checkout_page = setup_checkout
    checkout_page.fill_checkout_info("<script>alert('XSS')</script>", "QA", "11000")
    expect(checkout_page.page).to_have_url("https://www.saucedemo.com/checkout-step-two.html")
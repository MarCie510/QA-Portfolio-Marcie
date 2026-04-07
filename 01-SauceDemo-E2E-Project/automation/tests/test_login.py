from playwright.sync_api import expect
import pytest

# SDW-1: Successful login with standard user
@pytest.mark.smoke
def test_valid_login(login_page):
    """
    ID: SDW-1
    Scenario: Verifies that a standard user can successfully log in and reach the products page.
    """
    login_page.navigate_to_login()
    login_page.login("standard_user", "secret_sauce")
    
    expect(login_page.page).to_have_url("https://www.saucedemo.com/inventory.html")
    expect(login_page.page.locator(".title")).to_have_text("Products")

# SDW-2: Access blocked for locked out user
@pytest.mark.edge_case
def test_locked_out_user(login_page):
    """
    ID: SDW-2
    Scenario: Verifies that a locked-out user receives the correct error message.
    """
    login_page.navigate_to_login()
    login_page.login("locked_out_user", "secret_sauce")
    
    error_text = login_page.get_error_message()
    assert "Epic sadface: Sorry, this user has been locked out" in error_text

# SDW-3: Login rejection due to invalid credentials
@pytest.mark.edge_case
def test_invalid_credentials(login_page):
    """
    ID: SDW-3
    Scenario: Verifies that the system denies access when provided with incorrect credentials.
    """
    login_page.navigate_to_login()
    login_page.login("non_existent_user", "wrong_password")
    
    error_text = login_page.get_error_message()
    assert "Username and password do not match" in error_text

# SDW-4: Mandatory fields validation (Username)
@pytest.mark.edge_case
def test_empty_username(login_page):
    """
    ID: SDW-4
    Scenario: Verifies that the system prompts for a username when the field is left empty.
    """
    login_page.navigate_to_login()
    login_page.login("", "secret_sauce")
    
    error_text = login_page.get_error_message()
    assert "Username is required" in error_text

# SDW-4: Mandatory fields validation (Password)
@pytest.mark.edge_case
def test_empty_password(login_page):
    """
    ID: SDW-4
    Scenario: Verifies that the system prompts for a password when the field is left empty.
    """
    login_page.navigate_to_login()
    login_page.login("standard_user", "")
    
    error_text = login_page.get_error_message()
    assert "Password is required" in error_text

# SDW-5: Protection of unauthenticated routes (BOLA)
@pytest.mark.security
def test_unauthorized_access(login_page):
    """
    ID: SDW-5
    Scenario: Verifies that the inventory page is not accessible without an active session.
    """
    login_page.page.goto("https://www.saucedemo.com/inventory.html")
    expect(login_page.page).to_have_url("https://www.saucedemo.com/")
    
    error_text = login_page.get_error_message()
    assert "You can only access '/inventory.html' when you are logged in." in error_text

# SDW-6: Session destruction on Logout
@pytest.mark.smoke
def test_logout(login_page):
    """
    ID: SDW-6
    Scenario: Verifies that a user can successfully log out and the session is terminated.
    """
    login_page.navigate_to_login()
    login_page.login("standard_user", "secret_sauce")
    login_page.logout()
    
    expect(login_page.page).to_have_url("https://www.saucedemo.com/")
    expect(login_page.page.locator("#login-button")).to_be_visible()

# SDW-7: SQL Injection prevention on Username field
@pytest.mark.security
def test_sql_injection_prevention(login_page):
    """
    ID: SDW-7
    Scenario: Verifies that the system prevents SQL Injection via the username field.
    """
    login_page.navigate_to_login()
    sql_payload = "admin' OR '1'='1"
    login_page.login(sql_payload, "password123")
    
    error_text = login_page.get_error_message()
    assert "Username and password do not match" in error_text

# SDW-8: Cross-Site Scripting (XSS) prevention on login
@pytest.mark.security
def test_xss_prevention(login_page):
    """
    ID: SDW-8
    Scenario: Verifies that the system prevents XSS attacks via the username field.
    """
    login_page.navigate_to_login()
    # Injecting a script tag as username
    xss_payload = "<script>alert('XSS')</script>"
    login_page.login(xss_payload, "password123")
    
    # Verify the system handles it as an invalid login attempt
    error_text = login_page.get_error_message()
    assert "Username and password do not match" in error_text

# SDW-9: Low performance user validation
@pytest.mark.edge_case
def test_performance_glitch_user(login_page):
    """
    ID: SDW-9
    Scenario: Validates system handles the performance glitch user.
    """
    login_page.navigate_to_login()
    login_page.login("performance_glitch_user", "secret_sauce")
    
    # Verifies successful login despite the delay
    expect(login_page.page).to_have_url("https://www.saucedemo.com/inventory.html", timeout=10000)
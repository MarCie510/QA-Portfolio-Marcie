import os
import pytest
from playwright.sync_api import expect

# 🟢 Happy Path (Smoke Test)
@pytest.mark.smoke
def test_valid_login(login_page):
    login_page.navigate_to_login()
    
    email = os.environ.get("LOGIN_EMAIL", "")
    password = os.environ.get("LOGIN_PASSWORD", "")
    login_page.login(email, password)
    
    # Validation: Check that the user is logged in successfully
    expect(login_page.page.locator("text=Logged in as")).to_be_visible()

# 🔴 Edge Case (Negative Test)
@pytest.mark.edge_case
def test_invalid_login(login_page):
    login_page.navigate_to_login()
    login_page.login("nonexistent_user@test.com", "wrong_password")
    
    # Validation: Verify that the error message contains the word "incorrect"
    msg = login_page.get_error_message()
    assert "incorrect" in msg
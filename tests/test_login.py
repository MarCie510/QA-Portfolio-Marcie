import re
from playwright.sync_api import Page, expect

def test_login_successful(page: Page):
    """
    Test Case: Login - Successful Access
    Description: Verify that a user can log in with valid credentials using the Happy Path.
    """
    
    # --- Step 1: Navigate to Auth Page ([Shared Step] logic) ---
    # We navigate directly to the login page to optimize execution time
    page.goto("https://automationexercise.com/login")
    
    # Validation: Ensure the 'Login to your account' header is visible
    expect(page.get_by_role("heading", name="Login to your account")).to_be_visible()

    # --- Step 2: Enter Credentials ---
    # Using 'data-qa' selectors provides stability against UI changes
    page.fill("input[data-qa='login-email']", "justtesting466@gmail.com")
    page.fill("input[data-qa='login-password']", "Password123!")

    # --- Step 3: Submit Login ---
    page.click("button[data-qa='login-button']")

    # --- Step 4: Validate Expected Results ---
    # 1. Verify that the user is logged in by checking the username in the navbar
    # Note: 'Marcie Test' is the name used during registration
    expect(page.get_by_text("Logged in as Marcie Test")).to_be_visible()
    
    # 2. Verify that the 'Logout' button is present, confirming an active session
    expect(page.get_by_role("link", name="Logout")).to_be_visible()
from playwright.sync_api import Page, expect

def test_login_invalid_password(page: Page):
    """
    Test Case: Login - Invalid Password
    Description: Verify that an error message is displayed when using a wrong password.
    """
    page.goto("https://automationexercise.com/login")
    
    # Credentials with wrong password
    page.fill("input[data-qa='login-email']", "justtesting466@gmail.com")
    page.fill("input[data-qa='login-password']", "WrongPass123!")
    page.click("button[data-qa='login-button']")

    # Validation: Error message should be visible
    error_msg = page.get_by_text("your email or password is incorrect!")
    expect(error_msg).to_be_visible()

def test_signup_already_exists(page: Page):
    """
    Test Case: Signup - Existing Email
    Description: Verify that a user cannot register with an email that is already in the system.
    """
    page.goto("https://automationexercise.com/signup")
    
    # Using the fixed email we already created
    page.fill("input[data-qa='signup-name']", "Marcie Test")
    page.fill("input[data-qa='signup-email']", "justtesting466@gmail.com")
    page.click("button[data-qa='signup-button']")

    # Validation: Specific error message for duplicates
    expect(page.get_by_text("Email Address already exist!")).to_be_visible()
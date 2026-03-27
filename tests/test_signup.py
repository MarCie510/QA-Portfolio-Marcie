import random
from playwright.sync_api import Page, expect

def test_signup_successful(page: Page):
    """
    Test Case: Register User - Successful Sign Up
    Description: Verify that a user can create an account with a dynamic email.
    """
    
    # --- Setup: Maximize Viewport ---
    page.set_viewport_size({"width": 1920, "height": 1080})

    # --- Data Preparation ---
    random_id = random.randint(1000, 9999)
    email = f"marcie_qa_{random_id}@test.com"
    name = "Marcie QA"
    password = "Password123!"

    # --- Step 1: Navigate to Auth Page ---
    page.goto("https://automationexercise.com/signup")
    expect(page.get_by_role("heading", name="New User Signup!")).to_be_visible()

    # --- Step 2: Initiate Registration ---
    page.fill("input[data-qa='signup-name']", name)
    page.fill("input[data-qa='signup-email']", email)
    page.click("button[data-qa='signup-button']")

    # --- Step 3: Fill Account Information ---
    expect(page.get_by_text("Enter Account Information")).to_be_visible()
    
    page.check("input[id='id_gender2']") # Mrs.
    page.fill("input[data-qa='password']", password)
    
    page.select_option("select[data-qa='days']", "15")
    page.select_option("select[data-qa='months']", "6") # June
    page.select_option("select[data-qa='years']", "1990")

    # --- Step 4: Fill Address Information ---
    page.fill("input[data-qa='first_name']", "Marcie")
    page.fill("input[data-qa='last_name']", "Test")
    page.fill("input[data-qa='address']", "Calle Falsa 123")
    page.select_option("select[data-qa='country']", "United States")
    page.fill("input[data-qa='state']", "Florida")
    page.fill("input[data-qa='city']", "Miami")
    page.fill("input[data-qa='zipcode']", "33101")
    page.fill("input[data-qa='mobile_number']", "555123456")

    # --- Step 5: Complete Registration ---
    page.click("button[data-qa='create-account']")

    # --- Step 6: Validate Account Created ---
    expect(page.get_by_text("ACCOUNT CREATED!")).to_be_visible()
    
    # Click Continue
    page.click("a[data-qa='continue-button']")

    # --- AD TRAP FIX ---
    # Sometimes a Google Ad (Vignette) intercepts the navigation.
    # If the URL contains '#google_vignette', we force navigation to the homepage.
    if "google_vignette" in page.url:
        page.goto("https://automationexercise.com")
    
    # Final check: Logged in as...
    expect(page.get_by_text(f"Logged in as {name}")).to_be_visible()
    
    # Optional: Delete account (cleanup) - commented out for now
    # page.click("a[data-qa='delete-account']")
    # expect(page.get_by_text("ACCOUNT DELETED!")).to_be_visible()
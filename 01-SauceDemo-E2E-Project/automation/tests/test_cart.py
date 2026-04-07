import pytest
from playwright.sync_api import expect
from pages.cart_page import CartPage

# SDW-23: Cart is empty on initial login (Edge Case)
@pytest.mark.edge_case
def test_cart_empty_on_login(login_page):
    """
    ID: SDW-23
    Scenario: Verify cart is empty and badge is not visible on first login.
    """
    login_page.navigate_to_login()
    login_page.login("standard_user", "secret_sauce")
    cart_page = CartPage(login_page.page)
    
    assert cart_page.get_badge_count() == 0

# SDW-18: Add single product to cart from inventory (Happy Path)
@pytest.mark.smoke
def test_add_single_product(login_page):
    """
    ID: SDW-18
    Scenario: Add one item and verify badge updates.
    """
    login_page.navigate_to_login()
    login_page.login("standard_user", "secret_sauce")
    
    login_page.page.locator("#add-to-cart-sauce-labs-backpack").click()
    cart_page = CartPage(login_page.page)
    
    assert cart_page.get_badge_count() == 1

# SDW-19: Add multiple products to cart
@pytest.mark.smoke
def test_add_multiple_products(login_page):
    """
    ID: SDW-19
    Scenario: Add two items and verify cart contains them.
    """
    login_page.navigate_to_login()
    login_page.login("standard_user", "secret_sauce")
    
    login_page.page.locator("#add-to-cart-sauce-labs-backpack").click()
    login_page.page.locator("#add-to-cart-sauce-labs-bike-light").click()
    
    cart_page = CartPage(login_page.page)
    assert cart_page.get_badge_count() == 2
    
    cart_page.go_to_cart()
    assert cart_page.get_cart_item_count() == 2

# SDW-20: Remove product from cart via inventory page
@pytest.mark.smoke
def test_remove_product_inventory(login_page):
    """
    ID: SDW-20
    Scenario: Add and then remove an item directly from the inventory page.
    """
    login_page.navigate_to_login()
    login_page.login("standard_user", "secret_sauce")
    
    login_page.page.locator("#add-to-cart-sauce-labs-backpack").click()
    login_page.page.locator("#remove-sauce-labs-backpack").click()
    
    cart_page = CartPage(login_page.page)
    assert cart_page.get_badge_count() == 0

# SDW-21: Remove product from cart via cart page
@pytest.mark.smoke
def test_remove_product_cart(login_page):
    """
    ID: SDW-21
    Scenario: Add item, go to cart, and remove it there.
    """
    login_page.navigate_to_login()
    login_page.login("standard_user", "secret_sauce")
    
    login_page.page.locator("#add-to-cart-sauce-labs-backpack").click()
    cart_page = CartPage(login_page.page)
    cart_page.go_to_cart()
    
    login_page.page.locator("#remove-sauce-labs-backpack").click()
    assert cart_page.get_cart_item_count() == 0

# SDW-22: Cart contents persist after navigating back to inventory
@pytest.mark.smoke
def test_cart_persistence(login_page):
    """
    ID: SDW-22
    Scenario: Add item, go to cart, go back to inventory, verify item remains.
    """
    login_page.navigate_to_login()
    login_page.login("standard_user", "secret_sauce")
    
    login_page.page.locator("#add-to-cart-sauce-labs-backpack").click()
    cart_page = CartPage(login_page.page)
    cart_page.go_to_cart()
    
    login_page.page.locator("#continue-shopping").click()
    assert cart_page.get_badge_count() == 1

# SDW-24: Proceed to checkout from cart (Happy Path)
@pytest.mark.smoke
def test_proceed_to_checkout(login_page):
    """
    ID: SDW-24
    Scenario: Click checkout from the cart page.
    """
    login_page.navigate_to_login()
    login_page.login("standard_user", "secret_sauce")
    
    login_page.page.locator("#add-to-cart-sauce-labs-backpack").click()
    cart_page = CartPage(login_page.page)
    cart_page.go_to_cart()
    login_page.page.locator(cart_page.checkout_button).click()
    
    expect(login_page.page).to_have_url("https://www.saucedemo.com/checkout-step-one.html")

# SDW-25: Checkout button disabled on empty cart (Edge Case)
@pytest.mark.edge_case
@pytest.mark.xfail(reason="Known bug: SauceDemo allows checkout with empty cart")
def test_checkout_empty_cart(login_page):
    """
    ID: SDW-25
    Scenario: Verify checkout behavior when cart is empty.
    """
    login_page.navigate_to_login()
    login_page.login("standard_user", "secret_sauce")
    
    cart_page = CartPage(login_page.page)
    cart_page.go_to_cart()
    
    login_page.page.locator(cart_page.checkout_button).click()
    expect(login_page.page).not_to_have_url("https://www.saucedemo.com/checkout-step-one.html")
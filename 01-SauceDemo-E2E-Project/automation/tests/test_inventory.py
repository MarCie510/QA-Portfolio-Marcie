import pytest
import re
from playwright.sync_api import expect
from pages.inventory_page import InventoryPage

# SDW-10: All products displayed on inventory page
@pytest.mark.smoke
def test_all_products_displayed(login_page):
    """
    ID: SDW-10
    Scenario: Validate that the inventory page loads and displays all 6 available products.
    """
    login_page.navigate_to_login()
    login_page.login("standard_user", "secret_sauce")
    
    inventory_page = InventoryPage(login_page.page)
    
    assert inventory_page.get_item_count() == 6

# SDW-11: Sort products by Name (A to Z)
@pytest.mark.smoke
def test_sort_name_a_to_z(login_page):
    """
    ID: SDW-11
    Scenario: Validate that products are sorted alphabetically in ascending order.
    """
    login_page.navigate_to_login()
    login_page.login("standard_user", "secret_sauce")
    
    inventory_page = InventoryPage(login_page.page)
    inventory_page.sort_products("az")
    
    names = inventory_page.get_all_item_names()
    assert names == sorted(names)

# SDW-12: Sort products by Name (Z to A)
@pytest.mark.smoke
def test_sort_name_z_to_a(login_page):
    """
    ID: SDW-12
    Scenario: Validate that products are sorted alphabetically in descending order.
    """
    login_page.navigate_to_login()
    login_page.login("standard_user", "secret_sauce")
    
    inventory_page = InventoryPage(login_page.page)
    inventory_page.sort_products("za")
    
    names = inventory_page.get_all_item_names()
    assert names == sorted(names, reverse=True)

# SDW-13: Sort products by Price (low to high)
@pytest.mark.smoke
def test_sort_price_low_to_high(login_page):
    """
    ID: SDW-13
    Scenario: Validate that products are sorted by ascending price.
    """
    login_page.navigate_to_login()
    login_page.login("standard_user", "secret_sauce")
    
    inventory_page = InventoryPage(login_page.page)
    inventory_page.sort_products("lohi")
    
    prices = inventory_page.get_all_item_prices()
    assert prices == sorted(prices)

# SDW-14: Sort products by Price (high to low)
@pytest.mark.smoke
def test_sort_price_high_to_low(login_page):
    """
    ID: SDW-14
    Scenario: Validate that products are sorted by descending price.
    """
    login_page.navigate_to_login()
    login_page.login("standard_user", "secret_sauce")
    
    inventory_page = InventoryPage(login_page.page)
    inventory_page.sort_products("hilo")
    
    prices = inventory_page.get_all_item_prices()
    assert prices == sorted(prices, reverse=True)

# SDW-15: Product detail page displays correct information
@pytest.mark.smoke
def test_product_detail_page(login_page):
    """
    ID: SDW-15
    Scenario: Validate that clicking a product opens its detail page.
    """
    login_page.navigate_to_login()
    login_page.login("standard_user", "secret_sauce")
    
    inventory_page = InventoryPage(login_page.page)
    inventory_page.page.locator(inventory_page.item_name).first.click()
    
    # Verify redirection and elements
    expect(inventory_page.page).to_have_url(re.compile(r".*inventory-item\.html.*"))
    expect(inventory_page.page.locator(".inventory_details_name")).to_be_visible()
    
    # Return to inventory
    inventory_page.page.locator("#back-to-products").click()
    expect(inventory_page.page).to_have_url("https://www.saucedemo.com/inventory.html")

# SDW-17: Visual glitch user displays broken images
@pytest.mark.edge_case
def test_visual_glitch_images(login_page):
    """
    ID: SDW-17
    Scenario: Validate that visual_user sees broken product images.
    """
    login_page.navigate_to_login()
    login_page.login("visual_user", "secret_sauce")
    
    inventory_page = InventoryPage(login_page.page)
    
    # Check if the broken image file (sl-404) is present in the src attribute
    images = inventory_page.page.locator(".inventory_item_img img").all()
    broken_images = [img for img in images if "sl-404" in img.get_attribute("src")]
    
    assert len(broken_images) > 0
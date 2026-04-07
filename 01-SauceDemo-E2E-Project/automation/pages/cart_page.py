from pages.base_page import BasePage

class CartPage(BasePage):
    """
    Page Object for the Shopping Cart.
    """
    def __init__(self, page):
        super().__init__(page)
        self.cart_icon = ".shopping_cart_link"
        self.cart_badge = ".shopping_cart_badge"
        self.cart_item = ".cart_item"
        self.checkout_button = "#checkout"

    def go_to_cart(self):
        """Clicks the cart icon to navigate to the cart page."""
        self.page.locator(self.cart_icon).click()

    def get_badge_count(self):
        """Returns the number on the cart badge, or 0 if empty."""
        badge = self.page.locator(self.cart_badge)
        return int(badge.inner_text()) if badge.is_visible() else 0
        
    def get_cart_item_count(self):
        """Returns the number of products listed in the cart."""
        return self.page.locator(self.cart_item).count()
from pages.base_page import BasePage

class InventoryPage(BasePage):
    """
    Page Object for the Inventory page.
    """
    def __init__(self, page):
        super().__init__(page)
        # Locators
        self.inventory_item = ".inventory_item"
        self.item_name = ".inventory_item_name"
        self.item_price = ".inventory_item_price"
        self.sort_dropdown = ".product_sort_container"

    def get_item_count(self):
        """Returns the total number of inventory items displayed."""
        return self.page.locator(self.inventory_item).count()

    def get_all_item_names(self):
        """Returns a list of all product names."""
        return self.page.locator(self.item_name).all_inner_texts()

    def get_all_item_prices(self):
        """Returns a list of all product prices as floats."""
        prices = self.page.locator(self.item_price).all_inner_texts()
        # Remove '$' and convert to float for correct sorting assertion
        return [float(price.replace('$', '')) for price in prices]

    def sort_products(self, sort_value):
        """Selects an option from the sort dropdown (e.g., 'az', 'za', 'lohi', 'hilo')."""
        self.page.locator(self.sort_dropdown).select_option(sort_value)
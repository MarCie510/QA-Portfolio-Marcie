from pages.base_page import BasePage

class CheckoutPage(BasePage):
    """
    Page Object for the Checkout flow.
    """
    def __init__(self, page):
        super().__init__(page)
        # Locators
        self.first_name = "#first-name"
        self.last_name = "#last-name"
        self.postal_code = "#postal-code"
        self.continue_button = "#continue"
        self.cancel_button = "#cancel"
        self.finish_button = "#finish"
        self.error_message = "[data-test='error']"
        self.subtotal_label = ".summary_subtotal_label"
        self.tax_label = ".summary_tax_label"
        self.total_label = ".summary_total_label"
        self.complete_header = ".complete-header"

    def fill_checkout_info(self, first, last, zip_code):
        """Fills the checkout form and clicks continue."""
        self.page.locator(self.first_name).fill(first)
        self.page.locator(self.last_name).fill(last)
        self.page.locator(self.postal_code).fill(zip_code)
        self.page.locator(self.continue_button).click()

    def get_error_message(self):
        """Returns the error message text."""
        return self.page.inner_text(self.error_message)

    def get_price_value(self, locator):
        """Extracts the float value from a price label."""
        text = self.page.inner_text(locator)
        return float(text.split("$")[-1])
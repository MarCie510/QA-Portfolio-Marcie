from playwright.sync_api import Page

class BasePage:
    """
    BasePage class acts as a wrapper for Playwright methods.
    It provides common functionality for all page objects.
    """
    def __init__(self, page: Page):
        self.page = page

    def navigate(self, url: str):
        """Navigates to a specific URL."""
        self.page.goto(url)

    def do_click(self, selector: str):
        """Clicks on an element identified by the selector."""
        self.page.click(selector)

    def do_fill(self, selector: str, text: str):
        """Clears the field and fills it with the provided text."""
        self.page.fill(selector, text)

    def get_element_text(self, selector: str) -> str:
        """Retrieves the inner text content of an element."""
        return self.page.locator(selector).inner_text()
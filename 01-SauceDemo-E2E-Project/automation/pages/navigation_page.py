from pages.base_page import BasePage

class NavigationPage(BasePage):
    """
    Page Object for Navigation and UI elements.
    """
    def __init__(self, page):
        super().__init__(page)
        self.burger_menu = "#react-burger-menu-btn"
        self.menu_wrap = ".bm-menu-wrap"
        self.all_items_link = "#inventory_sidebar_link"
        self.about_link = "#about_sidebar_link"
        self.reset_link = "#reset_sidebar_link"
        self.twitter_link = "[data-test='social-twitter']"
        self.facebook_link = "[data-test='social-facebook']"
        self.linkedin_link = "[data-test='social-linkedin']"

    def open_menu(self):
        """Opens the hamburger menu."""
        self.page.locator(self.burger_menu).click()
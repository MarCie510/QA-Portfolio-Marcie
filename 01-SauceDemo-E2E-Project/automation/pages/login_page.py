from pages.base_page import BasePage

class LoginPage(BasePage):
    """
    Page Object for the Login page. 
    Contains all locators and actions for this specific page.
    """
    
    def __init__(self, page):
        super().__init__(page)
        # Locators
        self.username_input = "#user-name"
        self.password_input = "#password"
        self.login_button = "#login-button"
        self.error_message_container = ".error-message-container"

    def navigate_to_login(self):
        """Navigates to the SauceDemo login page."""
        self.page.goto("https://www.saucedemo.com/")

    def login(self, username, password):
        """Performs login action."""
        self.page.fill(self.username_input, username)
        self.page.fill(self.password_input, password)
        self.page.click(self.login_button)

    def get_error_message(self):
        """Returns the text of the error message if visible."""
        return self.page.inner_text(self.error_message_container)

    def logout(self):
        """
        Performs logout by clicking the burger menu and then the logout link.
        """
        # Click the burger menu button
        self.page.click("#react-burger-menu-btn")
        # Click the logout link in the sidebar
        self.page.click("#logout_sidebar_link")
from pages.base_page import BasePage

class LoginPage(BasePage):
    URL = "https://automationexercise.com/login"

    def __init__(self, page):
        super().__init__(page)
        # Selectores estables usando data-qa (Best Practice)
        self.email_input = "input[data-qa='login-email']"
        self.password_input = "input[data-qa='login-password']"
        self.login_btn = "button[data-qa='login-button']"
        # Selector para mensaje de error (login fallido)
        self.error_msg_params = "form[action='/login'] p"

    def navigate_to_login(self):
        self.navigate(self.URL)

    def login(self, email, password):
        self.do_fill(self.email_input, email)
        self.do_fill(self.password_input, password)
        self.do_click(self.login_btn)

    def get_error_message(self):
        return self.get_element_text(self.error_msg_params)

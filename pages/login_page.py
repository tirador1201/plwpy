'''
Login page
'''
from framework.base_page import BasePage


class LoginPage(BasePage):
    '''
    Class for elements on the login page
    '''
    def __init__(self, base, new_context=False):
        if new_context:
            super().__init__(base.browser)
        else:
            self.page = base.page
        self.email_txb = self.page.locator('#username')
        self.code_txb = self.page.locator('#code')
        self.log_in_btn = self.page.locator("//button[.='Log in']")
        self.continue_btn = self.page.locator("//button[.='Continue']")

    def input_email(self, email):
        self.email_txb.type(email)
        self.log_in_btn.click()

    def input_code(self, code_from_email):
        self.code_txb.type(code_from_email)
        self.continue_btn.click()

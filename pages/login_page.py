'''
Login page
'''
from framework.base_page import BasePage


class LoginPage(BasePage):
    '''
    Class for elements on the login page
    '''
    def __init__(self, base, new_context=False):
        super().__init__(new_context)
        self.page = base.page
        self.logo = self.page.locator('.b-top-logo')

    def click_logo(self):
        '''
        Click the main site logo
        :return:
        '''
        self.logo.click()
        self.page.wait_for_load_state()

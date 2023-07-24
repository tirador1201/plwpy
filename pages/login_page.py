'''
Login page
'''
from framework.base_page import BasePage


class LoginPage(BasePage):
    '''
    Class for elements on the login page
    '''
    def __init__(self, app, new_context=False):
        super().__init__(new_context)
        self.page = app.page

    def click_logo(self):
        '''
        Click the main site logo
        :return:
        '''
        self.page.query_selector('.b-top-logo').click()

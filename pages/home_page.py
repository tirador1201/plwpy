from framework.base_page import BasePage

class HomePage(BasePage):
    '''
    Describes elements on the homepage (the main site page)
    '''
    def __init__(self, base, new_context=False):
        if new_context:
            super().__init__(base.browser)
        else:
            self.page = base.page
        self.enroll_now_btn = self.page.locator("//a[@data-element-id='HEADER_BUTTON_ENROLL_NOW']")
        self.get_started_btn = self.page.locator("//a[@data-element-id='HOMEPAGE_LINK_WELCOME_ENROLL_CTA']")


    def enroll_now(self):
        '''
        Enroll to the company
        :return:
        '''
        self.enroll_now_btn.first.click()

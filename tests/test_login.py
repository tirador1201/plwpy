from playwright.sync_api import expect

from pages.home_page import HomePage
from pages.login_page import LoginPage


class TestLogin:
    def test_login(self, initial_page):
        home_page = HomePage(initial_page)
        home_page.enroll_now()
        # make sure login page is opened
        login_page = LoginPage(initial_page)
        expect(login_page.page).to_have_title('Log in | Test Company ESPP')
        # input email
        login_page.input_email("zomqok@rover.info")
        # check login code page is opened
        expect(login_page.page).to_have_title('Enter the code | Test Company ESPP')
        # input code
        login_page.input_code('123')

        print('')

    def test_login2(self, initial_page):
        login_page = LoginPage(initial_page)
        login_page.click_logo()
        print('Logging is here')

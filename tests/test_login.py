from playwright.sync_api import expect

from pages.home_page import HomePage
from pages.login_page import LoginPage


class TestLogin:
    def test_login(self, initial_page, generate_magic_link):
        email = generate_magic_link
        home_page = HomePage(initial_page)
        home_page.enroll_now()
        # make sure login page is opened
        login_page = LoginPage(initial_page)
        expect(login_page.page).to_have_title('Log in | Test Company ESPP')
        # input email
        login_page.input_email(email)
        # check login code page is opened
        expect(login_page.page).to_have_title('Enter the code | Test Company ESPP')
        # input code
        login_page.input_code('123')
        print('')

    def test_login2(self, generate_magic_link, initial_page, browser_name):
        email = generate_magic_link
        home_page = HomePage(initial_page)
        print(email)

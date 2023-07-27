from playwright.sync_api import expect

from framework.logger import log_text
from pages.home_page import HomePage
from pages.login_page import LoginPage


class TestLogin:
    def test_login(self, initial_page, generate_magic_link):
        email = generate_magic_link
        home_page = HomePage(initial_page)
        home_page.enroll_now()
        log_text("Make sure logging page is opened")
        login_page = LoginPage(initial_page)
        expect(login_page.page).to_have_title('Log in | Test Company ESPP')
        log_text("Input an email")
        login_page.input_email(email)
        log_text("Check login code page is opened")
        expect(login_page.page).to_have_title('Enter the code | Test Company ESPP')
        log_text("Input code")
        login_page.input_code('123')
        log_text('')

    def test_login2(self, home_page):
        page1 = home_page
        log_text('123')

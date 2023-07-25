from pages.login_page import LoginPage


class TestLogin:
    def test_login(self, initial_page):
        login_page = LoginPage(initial_page)
        login_page.click_logo()
        print('Logging is here')

    def test_login2(self, initial_page):
        login_page = LoginPage(initial_page)
        login_page.click_logo()
        print('Logging is here')

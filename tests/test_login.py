from pages.login_page import LoginPage


def test_login(initial_page):
    login_page = LoginPage(initial_page)
    login_page.click_logo()
    print('Logging is here')

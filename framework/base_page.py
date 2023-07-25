from playwright.sync_api import Browser


class BasePage:
    def __init__(self, new_context, browser: Browser = '', base_url: str = '', **kwargs):
        if new_context:
            self.browser = browser
            self.context = self.browser.new_context(**kwargs)
            self.base_url = base_url
            self.page = self.context.new_page()

    def goto(self, endpoint: str, use_base_url=True):
        if use_base_url:
            self.page.goto(self.base_url + endpoint)
        else:
            self.page.goto(endpoint)


    def close(self):
        self.page.close()
        self.context.close()

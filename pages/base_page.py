from playwright.sync_api import Page

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def navigate_to(self, url: str):
        self.page.goto(url)

    def click_element(self, selector: str):
        self.page.click(selector)

    # Elements sometimes are covered by styling or other elements
    # should not be used as a default, does not mimic human interaction,
    # but is necessary for some elements on this site
    def force_click_element(self, selector: str):
        self.page.click(selector, force=True)

    def send_keys(self, selector:str, keys:str):
        self.page.locator(selector).fill(keys)
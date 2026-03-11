from playwright.sync_api import Page
from pages.base_page import BasePage

# Only to navigate to the login page for the rest of the exercise
class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        # locators
        self.join_now_button = "//div[@class='auth-form__text']//a[@href]"

    def navigate_to_login_page(self):
        self.navigate_to("https://dittomusic.com/en/login")

    def click_join_now_button(self):
        self.click_element(self.join_now_button)
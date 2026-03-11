from playwright.sync_api import Page
from pages.base_page import BasePage

class SignUpPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        # locators
        self.email = "//input[@id='fc-EmailAddress']"
        self.invalid_email_message = "//input[@id='fc-EmailAddress']//following-sibling::div[@class='invalid-feedback']"
        self.password = "//input[@id='fc-Password']"
        self.invalid_password_message = "//input[@id='fc-Password']//following-sibling::div[@class='invalid-feedback']"
        self.marketing_checkbox = "(//input[@type='checkbox'])[1]"
        self.terms_checkbox = "(//input[@type='checkbox'])[2]"
        self.sign_up_button = "//button[@type='submit']"
        self.captcha = "iframe[title*='recaptcha challenge']"

    def enter_email(self, email:str):
        self.send_keys(self.email, email)

    def enter_password(self, password:str):
        self.send_keys(self.password, password)

    def click_marketing_checkbox(self):
        self.force_click_element(self.marketing_checkbox)

    def click_terms_checkbox(self):
        self.force_click_element(self.terms_checkbox)

    def click_sign_up_button(self):
        self.click_element(self.sign_up_button)

    def get_captcha_element(self):
        return self.page.locator(self.captcha).locator("visible=true")
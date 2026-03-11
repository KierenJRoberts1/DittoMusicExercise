from playwright.sync_api import expect
from pages.login_page import LoginPage
from pages.sign_up_page import SignUpPage
from faker import Faker

def test_valid_sign_up(sign_up_page: SignUpPage, login_page: LoginPage):
    fake = Faker()
    email = fake.email()
    password = fake.password()

    login_page.navigate_to_login_page()
    login_page.click_join_now_button()

    sign_up_page.enter_email(email)
    sign_up_page.enter_password(password)
    sign_up_page.click_marketing_checkbox()
    sign_up_page.click_terms_checkbox()
    sign_up_page.click_sign_up_button()

    expect(sign_up_page.get_captcha_element()).to_be_visible()

def test_invalid_email(sign_up_page: SignUpPage, login_page: LoginPage):
    fake = Faker()
    password = fake.password()

    login_page.navigate_to_login_page()
    login_page.click_join_now_button()

    sign_up_page.enter_email("invalid-email")
    sign_up_page.enter_password(password)

    expect(sign_up_page.page.locator(sign_up_page.invalid_email_message)).to_be_visible()

def test_invalid_password(sign_up_page: SignUpPage, login_page: LoginPage):
    fake = Faker()
    email = fake.email()

    login_page.navigate_to_login_page()
    login_page.click_join_now_button()

    sign_up_page.enter_email(email)
    sign_up_page.enter_password("aa")
    sign_up_page.click_terms_checkbox()

    expect(sign_up_page.page.locator(sign_up_page.invalid_password_message)).to_be_visible()
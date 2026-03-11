import pytest
from pages.login_page import LoginPage
from pages.sign_up_page import SignUpPage

@pytest.fixture
def sign_up_page(page):
    return SignUpPage(page)

@pytest.fixture
def login_page(page):
    return LoginPage(page)
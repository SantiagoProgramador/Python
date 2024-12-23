"""
Import the log in page
"""
from pages.log_in_page import LoginPage
import pytest

@pytest.mark.usefixtures("driver")
def log_in(driver,email,password):
    """First step to any test, Log in to the desired account"""

    log_in_page = LoginPage(driver)
    log_in_page.open()
    log_in_page.enter_email(email)
    log_in_page.click_next()
    log_in_page.enter_password(password)
    log_in_page.enter_phone_code()
    log_in_page.click_keep_signed()

    assert log_in_page.is_logged_in(email)

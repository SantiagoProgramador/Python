import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.base_page import BasePage
from config.test_settings import USERNAME, PASSWORD

@pytest.fixture
def driver():
    """
    Pytest fixture to create and yield a WebDriver instance.
    """
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_log_in(driver):
    """
    Test to validate the login functionality of the application.
    """
    base_page = BasePage(driver)
    base_page.login(USERNAME, PASSWORD)
   

    # Add an assertion to verify successful login
    assert "Home" in driver.title  # Replace with actual title after login

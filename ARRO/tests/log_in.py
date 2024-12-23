"""
This imports are needed so the webdriver can be run
"""
import time
from utils.base import LoginPageSelectors
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()

def test_log_in(username,password):
    """
    This function validate the title of the get page
    """
    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://isf-arro-qa-logstat.azurewebsites.net/")
    driver.maximize_window()
    email_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(LoginPageSelectors.EMAIL_INPUT)
    )
    email_field.send_keys(username)
    next_button = driver.find_element(*LoginPageSelectors.NEXT_BUTTON)
    next_button.click()
    time.sleep(2)
    password_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(LoginPageSelectors.PASSWORD_INPUT)
    )
    password_field.send_keys(password)
    password_field.send_keys(Keys.RETURN)
    print("Use your phone to place the code")
    time.sleep(14)
    keep_signed_in_button = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located(LoginPageSelectors.KEEP_SIGNED_BUTTON)
    )
    keep_signed_in_button.click()

"""
  Imports
"""
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class LoginPage:
    """    
    Represents the login page of the application
    """
    EMAIL_INPUT = (By.ID, "i0116")
    NEXT_BUTTON = (By.ID, "idSIButton9")
    PASSWORD_INPUT = (By.NAME, "passwd")
    KEEP_SIGNED_BUTTON = (By.ID, "idSIButton9")
    URL = "https://isf-arro-qa-logstat.azurewebsites.net/"

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        """Opens the login page"""
        self.driver.get(self.URL)

    def enter_email(self, email):
        """Enter the email"""
        email_input = self.driver.find_element(*self.EMAIL_INPUT)
        email_input.clear()
        email_input.send_keys(email)

    def click_next(self):
        """Click the 'Next' button"""
        next_button = self.driver.find_element(*self.NEXT_BUTTON)
        next_button.click()

    def enter_password(self, password):
        """Enter the password"""
        password_input = self.driver.find_element(*self.PASSWORD_INPUT)
        password_input.clear()
        password_input.send_keys(password)

    def enter_phone_code(self):
        """Enter the phone code, not implemented yet, must be manually entered"""
        print("Use your phone to get the code and enter it manually...")
        time.sleep(20)

    def click_keep_signed(self):
        """Click the 'Keep me signed in' button"""
        keep_signed_button = self.driver.find_element(*self.KEEP_SIGNED_BUTTON)
        keep_signed_button.click()

    def is_logged_in(self,email):
        """Verify that the user is logged in"""
        try:
            account = WebDriverWait(self.driver,10).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//body//nav//ul[@class='navbar-nav navbar-right']/li/span[4]"))
            )
            is_logged_in = account.text == email
            return is_logged_in
        except TimeoutException:
            return False

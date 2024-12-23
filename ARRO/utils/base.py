"""
Global variables
"""
from selenium.webdriver.common.by import By

URL = "https://isf-arro-qa-logstat.azurewebsites.net/"


class LoginPageSelectors:
    """
    Class to define the Log in selectors
    """
    EMAIL_INPUT = (By.ID, "i0116")
    NEXT_BUTTON = (By.ID, "idSIButton9")
    PASSWORD_INPUT = (By.NAME, "passwd")
    KEEP_SIGNED_BUTTON = (By.ID, "idSIButton9")

class HomePageSelectors:
    """
    Class to define home page selectors
    """
    URL = "https://isf-arro-qa-logstat.azurewebsites.net/"

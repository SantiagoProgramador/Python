from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from config.test_settings import USERNAME, PASSWORD
from utils.test_base import LoginPageSelectors  # Importamos los selectores de login

class BasePage:
    """
    Base page to manage common page functionalities, including login.
    """
    URL = "https://isf-arro-qa-logstat.azurewebsites.net/"

    # Usamos los selectores de LoginPageSelectors
    EMAIL_INPUT = LoginPageSelectors.EMAIL_INPUT
    NEXT_BUTTON = LoginPageSelectors.NEXT_BUTTON
    PASSWORD_INPUT = LoginPageSelectors.PASSWORD_INPUT
    KEEP_SIGNED_BUTTON = LoginPageSelectors.KEEP_SIGNED_BUTTON

    def __init__(self, driver):
        self.driver = driver

    @staticmethod
    def create_driver():
        """
        Creates and returns a new instance of the Chrome WebDriver.
        """
        service = Service(ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        driver = webdriver.Chrome(service=service, options=options)
        return driver

    def login(self, username=USERNAME, password=PASSWORD):
        """
        Reusable method for logging into the application.
        """
        self.driver.get(self.URL)

        # Espera explícita para asegurar que el campo de correo esté visible
        email_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.EMAIL_INPUT)
        )
        email_field.send_keys(username)

        # Espera explícita para el botón "Next"
        next_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.NEXT_BUTTON)
        )
        next_button.click()

        # Espera explícita para el campo de contraseña
        password_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.PASSWORD_INPUT)
        )
        password_field.send_keys(password)
        password_field.send_keys(Keys.RETURN)
        
        login_button = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable(self.KEEP_SIGNED_BUTTON)
        )
        login_button.click()

        print("Please complete the code verification on your phone.")
        
        # Esperar a que el usuario ingrese el código manualmente
        input("Por favor, completa la verificación de código en tu teléfono y presiona Enter para continuar...")

        # Re-obtenemos la referencia al botón "Keep me signed in" después de que la página se haya actualizado
        keep_signed_in_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.KEEP_SIGNED_BUTTON)
        )
        keep_signed_in_button.click()

        # Esperamos que la página de Dashboard esté disponible
        WebDriverWait(self.driver, 10).until(
            EC.title_contains("Home")  # Verifica si el título contiene "Dashboard"
        )
       

# En tu archivo de test, por ejemplo en `test_log_in.py`:
def test_log_in(driver):
    """
    Test to validate the login functionality of the application.
    """
    base_page = BasePage(driver)
    base_page.login(USERNAME, PASSWORD)

    # Ahora verificamos que el título contenga "Dashboard"
    assert "Home" in driver.title

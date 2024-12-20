"""
This imports are needed so the webdriver can be run
"""
import time
from utils.base import EMAIL_INPUT_ID, PASSWORD_INPUT_NAME, NEXT_BUTTON_ID, KEEP_SIGNED_BUTTON
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()

def log_in(username,password):
    """
    This function validate the title of the get page
    """
    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://isf-arro-qa-logstat.azurewebsites.net/")
    driver.maximize_window()
    email_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, EMAIL_INPUT_ID))
    )
    email_field.send_keys(username)
    next_button = driver.find_element(By.ID, NEXT_BUTTON_ID)
    next_button.click()
    time.sleep(2)
    password_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, PASSWORD_INPUT_NAME))
    )
    password_field.send_keys(password)
    password_field.send_keys(Keys.RETURN)
    print("Use your phone to place the code")
    time.sleep(14)
    keep_signed_in_button = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, KEEP_SIGNED_BUTTON))
    )
    keep_signed_in_button.click()
    time.sleep(3)
    get_text = WebDriverWait(driver,40).until(
        EC.presence_of_element_located(
            (By.XPATH,"/html/body/div[6]/main/footer/p[text()='© 2024']")))
    if get_text.is_displayed():
        print("Successful access")
    else:
        print("Unsuccessful access")
    driver.quit()

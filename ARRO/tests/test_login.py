"""
This imports are needed so the webdriver can be run
"""
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()


def log_in():
    """
    This function validate the title of the get page
    """
    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://isf-arro-qa-logstat.azurewebsites.net/")
    driver.maximize_window()
    email_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "i0116"))
    )
    email_field.send_keys("santiago.lara@blackbirdlabs.com.co")
    next_button = driver.find_element(By.ID, "idSIButton9")
    next_button.click()
    time.sleep(3)
    password_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "passwd"))
    )
    password_field.send_keys("49608817QA.")
    password_field.send_keys(Keys.RETURN)
    print("Use your phone to place the code")
    time.sleep(30)
    keep_signed_in_button = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "idSIButton9"))
    )
    keep_signed_in_button.click()
    time.sleep(5)
    get_text = WebDriverWait(driver,40).until(
        EC.presence_of_element_located(
            (By.XPATH,"/html/body/div[6]/main/footer/p[text()='© 2024']")))
    if get_text.is_displayed():
        print("Successful access")
    else:
        print("Unsuccessful access")
    
    driver.quit()

log_in()

"""
Importing email and password from a .env
Must create a .env file with the following format:
MY_APP_EMAIL = your email
MY_APP_PASS = your password
"""
import os
from dotenv import load_dotenv

load_dotenv()

EMAIL = os.getenv("MY_APP_EMAIL")
PASSWORD = os.getenv("MY_APP_PASS")

if not EMAIL or not PASSWORD:
    print("Error: Please set the MY_APP_EMAIL and MY_APP_PASS environment variables.")

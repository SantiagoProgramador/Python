"""
Importing necessary libraries and modules
"""
import os
from dotenv import load_dotenv

load_dotenv()

USERNAME = os.getenv("MY_APP_USER")
PASSWORD = os.getenv("MY_APP_PASS")

if not USERNAME or not PASSWORD:
    print("Error: Please set the MY_APP_USER and MY_APP_PASS environment variables.")

"""
Importing credentials
"""
from config.settings import USERNAME, PASSWORD
from tests.log_in import test_log_in

def connect_to_service():
    """
    Validate provided credentials.
    """
    print("Connecting...")
    print(f"User: {USERNAME}")
    print("Connection successful.")

if __name__ == "__main__":
    connect_to_service()
    test_log_in(USERNAME,PASSWORD)

"""
Importing necessary libraries and modules**
"""
from tests.log_in import log_in
from config.settings import EMAIL,PASSWORD
import pytest

@pytest.mark.usefixtures("driver")
def test_import(driver):
    """
    Function to test the import functionality
    """
    log_in(driver, EMAIL,PASSWORD)

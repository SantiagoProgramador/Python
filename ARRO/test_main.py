"""
Tests for validating application login.
"""
import pytest
from config.test_settings import USERNAME, PASSWORD

def test_connect_to_service():
    """
    Validate the presence of credentials.
    """
    assert USERNAME, "USERNAME is not set."
    assert PASSWORD, "PASSWORD is not set."
    print(f"Connecting with USERNAME: {USERNAME}")

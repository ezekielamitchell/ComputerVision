import pytest

def pytest_configure(config):
    """Register custom marks."""
    config.addinivalue_line(
        "markers",
        "manual: mark test as a manual test that requires human interaction"
    ) 
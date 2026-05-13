import pytest

@pytest.fixture 
def open_homepage(page):
    page.goto("/")
    return page
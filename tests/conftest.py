import pytest
from app import duties

@pytest.fixture(autouse=True)
def reset_duties():
    global duties
    duties.clear()   

@pytest.fixture 
def open_homepage(page):
    page.goto("/")
    return page
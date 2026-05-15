import pytest
from app import app

@pytest.fixture(autouse=True)
def reset_duties():
    app.service.duties.clear()   

@pytest.fixture 
def open_homepage(page):
    page.goto("/")
    return page
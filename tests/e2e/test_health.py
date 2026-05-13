def test_app_is_running(page):
    response = page.goto('http://localhost:5000')
    assert response.ok
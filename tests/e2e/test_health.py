def test_app_is_running(page):
    response = page.goto('/')
    assert response.ok
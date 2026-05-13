def test_homepage_has_automate_coin_title(page):
    page.goto("http://localhost:5000")

    assert "Automate Coin" in page.content()
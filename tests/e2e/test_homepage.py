from playwright.sync_api import expect


def test_homepage_has_automate_coin_title(page):
    page.goto("http://localhost:5000")

    assert "Automate Coin" in page.content()

def test_homepage_has_h1(page):
    page.goto("http://localhost:5000")

    expect(page.locator("h1")).to_contain_text("Automate Coin")

def test_duties_section_exists(page):
    page.goto("http://localhost:5000")

    expect(page.locator("#duties-section")).to_be_attached()
from playwright.sync_api import expect


def test_homepage_has_automate_coin_title(open_homepage):
    assert "Automate Coin" in open_homepage.content()

def test_homepage_has_h1(open_homepage):
    expect(open_homepage.locator("h1")).to_contain_text("Automate Coin")

def test_duties_section_exists(page):
    page.goto("http://localhost:5000")

    expect(page.locator("#duties-section")).to_be_visible()

def test_duty_input_exists(page):
    page.goto("http://localhost:5000")

    expect(page.locator("#duty-number-input")).to_be_visible()

def test_duty_number_input_has_label(page):
    page.goto("http://localhost:5000")

    expect(page.get_by_label("Duty Number")).to_be_visible()

def test_duty_description_exists(page):
    page.goto("http://localhost:5000")

    expect(page.locator("#duty-description-input")).to_be_visible()

def test_duty_description_input_has_label(page):
    page.goto("http://localhost:5000")

    expect(page.get_by_label("Duty Description")).to_be_visible()

def test_add_duty_button_exists(open_homepage):
    expect(open_homepage.get_by_role("button", name="Add Duty")).to_be_visible()



from playwright.sync_api import expect

def test_user_can_add_a_duty(open_homepage):
    page = open_homepage
    page.fill("#duty-number-input", "1")
    page.fill("#duty-description-input", "My First Duty")
    page.click("text=Add Duty")

    expect(page.locator("#duties-list")).to_contain_text("1 - My First Duty")

def test_user_cannot_add_duplicate_duty_number(open_homepage):
    page = open_homepage

    # first duty
    page.fill("#duty-number-input", "1")
    page.fill("#duty-description-input", "First Duty")
    page.click("text=Add Duty")

    # dupicate duty number
    page.fill("#duty-number-input", "1")
    page.fill("#duty-description-input", "Duplicate Duty")
    page.click("text=Add Duty")

    expect(page.locator("#duties-list")).not_to_contain_text("1 - Duplicate Duty")

def test_user_cannont_add_empty_duty(open_homepage):
    page = open_homepage
    page.click("text=Add Duty")

    expect(page.locator("#duties-list")).to_be_empty()

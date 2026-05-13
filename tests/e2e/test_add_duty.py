from playwright.sync_api import expect

def test_user_can_add_a_duty(open_homepage):
    page = open_homepage
    page.fill("#duty-number-input", "1")
    page.fill("#duty-description-input", "My First Duty")
    page.click("text=Add Duty")

    expect(page.locator("#duties-list")).to_contain_text("1 - My First Duty")
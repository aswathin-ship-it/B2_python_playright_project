from playwright.sync_api import expect

def test_sync_exp3(page):
    page.goto("https://www.facebook.com/")


    expect(page).to_have_title("Facebook")
    expect(page).to_have_url("https://www.facebook.com/")

    page.goto("https://www.amazon.in/")

    expect(page).to_have_url("https://www.amazon.in/")

    page.go_back()

    expect(page).to_have_url("https://www.facebook.com/")

    page.go_forward()

    expect(page).to_have_url("https://www.amazon.in/")

    page.reload()
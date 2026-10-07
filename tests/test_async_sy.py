

# Sync Playwright
#def test_sync_exp1():
 #  with sync_playwright() as p:
 #   browser = p.chromium.launch(headless=False)
 #
 # user_context = browser.new_context()
 #  page = user_context.new_page()
 #
 #  page.goto("https://www.facebook.com/")
 #
 #  print(page.title())
 #
 # sync_expect(page).to_have_title("Facebook")
 # browser.close()


# Async Playwright
async def test_async_exp2():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)

        user_context = await browser.new_context()

        page = await user_context.new_page()

        await page.goto("https://www.facebook.com/")

        print(await page.title())

        await expect(page).to_have_title("Facebook")

        await browser.close()
        asyncio.run(test_async_exp2())

from playwright.sync_api import expect
def test_sync_exp3(page):
    page.goto("https://www.facebook.com/")

    print(page.title())

    # Check page title
    expect(page).to_have_title("Facebook")

    # Check current URL
    expect(page).to_have_url("https://www.facebook.com/")

    # Go back
    page.go_back()

    # Go forward
    page.go_forward()

    # Reload the page
    page.reload()
    import pytest
    from playwright.async_api import expect

    @pytest.mark.asyncio
    async def test_async_exp4(page):
        await page.goto("https://www.facebook.com/")
        print(await page.title())
        await expect(page).to_have_title("Facebook")

import pytest
from playwright.async_api import async_playwright


@pytest.mark.asyncio
async def test_user_context():
    async with async_playwright() as p:

        browser = await p.chromium.launch(headless=False)

        # Create user context
        context = await browser.new_context()

        # Page 1
        page1 = await context.new_page()
        await page1.goto("https://www.google.com")
        print("Page 1:", await page1.title())

        # Page 2
        page2 = await context.new_page()
        await page2.goto("https://www.facebook.com")
        print("Page 2:", await page2.title())

        # Page 3
        page3 = await context.new_page()
        await page3.goto("https://www.amazon.in/")
        print("Page 3:", await page3.title())

        await context.close()
        await browser.close()
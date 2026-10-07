import pytest
from playwright.async_api import async_playwright


@pytest.mark.asyncio
async def test_diff_browsers():

    async with async_playwright() as p:

        # Chromium
        chromium_browser = await p.chromium.launch(headless=False)
        chromium_context = await chromium_browser.new_context()
        chromium_page = await chromium_context.new_page()

        await chromium_page.goto("https://www.google.com")
        print("Chromium:", await chromium_page.title())

        await chromium_browser.close()


        # Firefox
        firefox_browser = await p.firefox.launch(headless=False)
        firefox_context = await firefox_browser.new_context()
        firefox_page = await firefox_context.new_page()

        await firefox_page.goto("https://www.amazon.in/")
        print("Firefox:", await firefox_page.title())

        await firefox_browser.close()


        # WebKit
        webkit_browser = await p.webkit.launch(headless=False)
        webkit_context = await webkit_browser.new_context()
        webkit_page = await webkit_context.new_page()

        await webkit_page.goto("https://www.wikipedia.org")
        print("WebKit:", await webkit_page.title())

        await webkit_browser.close()
import pytest
@pytest.mark.asyncio
async def test_date_picker(async_page):
    await async_page.goto("https://jqueryui.com/datepicker/")
    fl = async_page.frame_locator("demo-frame")
    date = fl.locator("//input[@id='datepicker']")
    await date.click()
    day = fl.locator("//a[text()='17']")
    await day.click()

import pytest
@pytest.mark.asyncio
async def test_date_picker(async_page):
    await async_page.goto("https://jqueryui.com/datepicker/")
    fl = async_page.frame_locator(".demo-frame")
    date = fl.locator("//input[@id='datepicker']")
    await date.click()
    day = fl.locator("//a[text()='17']")
    await day.click()
    #//input[@id='datepicker']


@pytest.mark.asyncio
async def test_date_picker(async_page):
    um = "December"
    uy = "2026"
    ud = "12"

    await async_page.goto("https://jqueryui.com/datepicker/")
    fl = async_page.frame_locator(".demo-frame")
    date = fl.locator("//input[@id='datepicker']")
    await date.click()

    cm = await fl.locator(".ui-datepicker-month").inner_text()
    cy = await fl.locator(".ui-datepicker-year").inner_text()
    print(cm)
    print(cy)
    while (True):
        if (uy == cy and um == cm):
            await fl.locator(f"//a[text()='{ud}']").click()
            break

        await fl.locator("//span[text()='Next']").click()
        cm = await fl.locator(".ui-datepicker-month").inner_text()
        cy = await fl.locator(".ui-datepicker-year").inner_text()
        await async_page.wait_for_timeout(5000)

@pytest.mark.asyncio
async def test_range_slider(async_page):
    await async_page.goto("https://jqueryui.com/resources/demos/slider/range.html?utm_source")
    min = 100
    max = 400

    slider = async_page.locator("//div[@id='slider-range']/span")
    await slider.nth(0).focus()
    await slider.nth(0).press("Home")

    for i in range(min):
        await slider.nth(0).press("ArrowRight")

    await slider.nth(1).focus()
    await slider.nth(1).press("End")
    for i in range(500,max):
        await slider.nth(0).press("ArrowLeft")
        await async_page.wait_for_timeout(5000)
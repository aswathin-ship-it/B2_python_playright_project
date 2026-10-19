import pytest

@pytest.mark.asyncio
async def test_end_to_end(async_page):
    await async_page.goto("https://demowebshop.tricentis.com/")

    # =============================================================================
    # ====================== Reg
    # =================================================================================
    await async_page.locator("//a[text()='Register']").click()
    await async_page.get_by_label("First name:").fill("abc")
    await async_page.get_by_label("Last name:").fill("abc")
    await async_page.get_by_label("Email:").fill("abcd1234@gmail.com")
    await async_page.get_by_label("Password:").nth(0).fill("abc@123")
    await async_page.get_by_label("Confirm password:").fill("abc@123")
    await async_page.locator("#register-button").click()

    try:
        await async_page.get_by_text("Log out").is_visible()

    except Exception:
          print(await async_page.locator("//span[@class='field-validation-error']").all_text_contents())

    # =============================================================================
    # ====================== login
    # =================================================================================
    await async_page.get_by_text("Log in").click()
    await async_page.get_by_label("Email:").fill("abcd1234@gmail.com")
    await async_page.get_by_label("Password:").fill("abc@123")
    await async_page.locator("//input[@value='Log in']").click()
    try:
        await async_page.get_by_text("Log out").is_visible()

    except Exception:
        print(await async_page.locator("//span[@class='field-validation-error']").all_text_contents())

#  ============================================================================================
#   =================== SEARCH
# ==============================================================================================
    await async_page.locator("#small-searchterms").fill("COMPUTER")
    await async_page.locator("//input[@value='Search']").click()
    product_name = ["Simple Computer","Build your own cheap computer"]
    for i in product_name:
        await async_page.locator(f"//a[text()='{i}']/../..//input[@value='Add to cart']").click()

    await async_page.get_by_text("Shopping cart").click()
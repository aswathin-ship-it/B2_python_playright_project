def test_for_open_page (page):
    page.goto("https://xml.onlineviewer.net/")
    page.wait_for_timeout(5000)
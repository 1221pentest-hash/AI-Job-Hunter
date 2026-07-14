from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)

    page = browser.new_page()

    page.goto("https://www.python.org")

    print("Title:", page.title())

    search_box = page.locator("#id-search-field")

    search_box.fill("playwright")

    page.keyboard.press("Enter")

    input("Press ENTER to close...")

    browser.close()
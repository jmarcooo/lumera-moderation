from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto('file:///app/packages.html')

    # View details
    page.evaluate('showDetail()')

    # Wait for the view-detail to become visible
    page.wait_for_selector('#view-detail', state='visible')

    # Click the reject radio button
    page.click('input[value="reject"]')

    page.screenshot(path='screenshot_packages_reject.png', full_page=True)

    browser.close()

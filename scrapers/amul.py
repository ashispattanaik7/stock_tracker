from playwright.sync_api import sync_playwright


def get_amul_status(url, pincode):

    with sync_playwright() as p:

        browser = p.chromium.launch(
            executable_path="/usr/bin/google-chrome",
            headless=True
        )

        page = browser.new_page()

        page.goto(url)

        page.locator("#search").fill(pincode)

        page.wait_for_timeout(2000)

        page.locator(".searchitem-name").first.click()

        page.wait_for_timeout(5000)

        availability = page.locator(
            '[itemprop="availability"]'
        ).get_attribute("href")

        browser.close()

        if availability and availability.endswith("OutOfStock"):
            return "OUT_OF_STOCK"

        elif availability and availability.endswith("InStock"):
            return "IN_STOCK"

        return "UNKNOWN"
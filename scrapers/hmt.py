from playwright.sync_api import sync_playwright


def get_hmt_status(url):

    with sync_playwright() as p:

        browser = p.chromium.launch(
            executable_path="/usr/bin/google-chrome",
            headless=True
        )

        page = browser.new_page()

        page.goto(
            url,
            timeout=60000
        )

        page.wait_for_timeout(5000)

        html = page.content()

        browser.close()

        if "<strong>Out Of Stock</strong>" in html:
            return "OUT_OF_STOCK"

        if "Add To Cart" in html:
            return "IN_STOCK"

        return "UNKNOWN"
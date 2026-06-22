from playwright.sync_api import sync_playwright


def get_hmt_store_status(url):

    with sync_playwright() as p:

        browser = p.chromium.launch(
            executable_path="/usr/bin/google-chrome",
            headless=False
        )

        try:

            page = browser.new_page()

            page.goto(
                url,
                wait_until="domcontentloaded",
                timeout=60000
            )

            page.wait_for_timeout(5000)

            buttons = page.locator(
                '[data-testid="buybuttonswidget-add-to-cart-button"]'
            )

            if buttons.count() == 0:
                return "UNKNOWN"

            button = buttons.first

            text = button.text_content()

            if text is None:
                return "UNKNOWN"

            text = text.strip().lower()

            if text == "out of stock":
                return "OUT_OF_STOCK"

            if text == "add to cart":
                return "IN_STOCK"

            return "UNKNOWN"

        except Exception as e:

            print(
                f"HMT Store Error: {e}"
            )

            return "UNKNOWN"

        finally:

            browser.close()
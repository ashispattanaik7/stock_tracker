from scrapers import get_status

from notifier import send_notification

from logger import (
    log,
    log_error
)

from database.db import (
    get_previous_status,
    save_status,
    get_scraper_health,
    save_scraper_health
)

from config.products import PRODUCTS


for product in PRODUCTS:

    scraper_name = product["scraper"]

    try:

        print()
        print("=" * 50)
        print(product["name"])

        previous_status = get_previous_status(
            product["name"]
        )

        current_status = get_status(product)

        if current_status == "UNKNOWN":

            log(
                f"WARNING | {product['name']} returned UNKNOWN"
            )

            print("UNKNOWN STATUS")

            continue

        # Scraper recovered?
        previous_health = get_scraper_health(
            scraper_name
        )

        if previous_health == "FAILED":

            send_notification(
                "Scraper Recovered",
                f"{scraper_name} scraper is working again"
            )

            log(
                f"SCRAPER RECOVERED | {scraper_name}"
            )

        save_scraper_health(
            scraper_name,
            "WORKING"
        )

        print("Previous:", previous_status)
        print("Current :", current_status)

        log(
            f"{product['name']} | "
            f"Previous={previous_status} | "
            f"Current={current_status}"
        )

        if (
            previous_status == "OUT_OF_STOCK"
            and current_status == "IN_STOCK"
        ):

            send_notification(
                "Stock Alert",
                f"{product['name']} is back in stock!"
            )

            print("ALERT SENT")

            log(
                f"ALERT SENT | "
                f"{product['name']} is back in stock"
            )

        else:
            print("NO ALERT")

        save_status(
            product["name"],
            product["url"],
            current_status
        )

    except Exception as e:

        error_message = (
            f"{product['name']} failed: {str(e)}"
        )

        print(error_message)

        log_error(error_message)

        previous_health = get_scraper_health(
            scraper_name
        )

        save_scraper_health(
            scraper_name,
            "FAILED"
        )

        # Notify only once when scraper first fails
        if previous_health != "FAILED":

            try:

                send_notification(
                    "Stock Tracker Error",
                    error_message
                )

            except Exception as notification_error:

                log_error(
                    f"Notification failed: "
                    f"{str(notification_error)}"
                )
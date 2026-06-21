import requests


def send_notification(
    title,
    message
):

    topic = "ashis-stock-tracker-2026"

    requests.post(
        f"https://ntfy.sh/{topic}",
        data=message.encode("utf-8"),
        headers={
            "Title": title
        },
        timeout=10
    )
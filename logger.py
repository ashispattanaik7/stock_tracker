from datetime import datetime


def log(message):

    timestamp = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    with open(
        "logs/tracker.log",
        "a",
        encoding="utf-8"
    ) as f:

        f.write(
            f"[{timestamp}] {message}\n"
        )


def log_error(message):

    timestamp = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    with open(
        "logs/errors.log",
        "a",
        encoding="utf-8"
    ) as f:

        f.write(
            f"[{timestamp}] {message}\n"
        )
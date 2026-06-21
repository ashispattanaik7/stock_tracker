import sqlite3
from datetime import datetime

from pathlib import Path

DB_PATH = Path("data/stock.db")


def get_previous_status(product_name):

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT status
        FROM products
        WHERE name = ?
        """,
        (product_name,)
    )

    row = cursor.fetchone()

    conn.close()

    if row:
        return row[0]

    return None


def save_status(
    product_name,
    url,
    status
):

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT OR REPLACE INTO products
        (
            name,
            url,
            status,
            last_checked
        )
        VALUES (?, ?, ?, ?)
        """,
        (
            product_name,
            url,
            status,
            datetime.now().isoformat()
        )
    )

    conn.commit()
    conn.close()

def get_scraper_health(scraper_name):

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT status
        FROM scraper_health
        WHERE scraper_name = ?
        """,
        (scraper_name,)
    )

    row = cursor.fetchone()

    conn.close()

    if row:
        return row[0]

    return None

def save_scraper_health(
    scraper_name,
    status
):

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT OR REPLACE INTO scraper_health
        (
            scraper_name,
            status,
            last_updated
        )
        VALUES (?, ?, ?)
        """,
        (
            scraper_name,
            status,
            datetime.now().isoformat()
        )
    )

    conn.commit()
    conn.close()
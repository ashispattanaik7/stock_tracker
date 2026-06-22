from .amul import get_amul_status
from .hmt import get_hmt_status
from .hmt_store import get_hmt_store_status


def get_status(product):

    scraper = product["scraper"]

    if scraper == "amul":

        return get_amul_status(
            product["url"],
            product["pincode"]
        )

    elif scraper == "hmt":

        return get_hmt_status(
            product["url"]
        )

    elif scraper == "hmt_store":

        return get_hmt_store_status(
            product["url"]
        )

    raise Exception(
        f"Unknown scraper: {scraper}"
    )
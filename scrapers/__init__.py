from .amul import get_amul_status


def get_status(product):

    scraper = product["scraper"]

    if scraper == "amul":

        return get_amul_status(
            product["url"],
            product["pincode"]
        )

    raise Exception(
        f"Unknown scraper: {scraper}"
    )
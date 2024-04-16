from pyalex import Institutions


def get_institutions() -> list[Institutions]:
    # Get 5 random institutions
    return [Institutions().random() for _ in range(5)]


def get_associated_institutions(institutions: list[Institutions]) -> list[Institutions]:
    # Gather associated institutions
    seen = set()
    associated_institutions = [
        y
        for x in institutions
        for y in x["associated_institutions"]
        if not (y["id"] in seen or seen.add(y["id"]))
    ]
    return associated_institutions


def dedup_institutions(institutions: list[Institutions]) -> list[Institutions]:
    seen = set()
    return [x for x in institutions if not (x["id"] in seen or seen.add(x["id"]))]

from pyalex import Institution, Institutions


def get_institutions() -> list[Institution]:
    # Get 5 random institutions for now
    return [Institutions().random() for _ in range(5)]


def get_associated_institutions(institutions: list[Institution]) -> list[Institution]:
    # Gather associated institutions
    seen = set()
    associated_institutions = [
        y
        for x in institutions
        for y in x["associated_institutions"]
        if not (y["id"] in seen or seen.add(y["id"]))
    ]
    return associated_institutions


def dedup_institutions(institutions: list[Institution]) -> list[Institution]:
    seen = set()
    return [x for x in institutions if not (x["id"] in seen or seen.add(x["id"]))]

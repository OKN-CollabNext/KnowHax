from pyalex import Author, Authors, Institution


def get_affiliated_authors(institutions: list[Institution]) -> list[Author]:
    seen = set()
    return [
        y
        for x in institutions
        for y in Authors().filter(affiliations={"institution": {"id": x["id"]}}).get()
        if not (y["id"] in seen or seen.add(y["id"]))
    ]

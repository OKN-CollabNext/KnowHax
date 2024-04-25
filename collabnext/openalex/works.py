from pyalex import Author, Institution, Work, Works


def get_works_by_authors(authors: list[Author]) -> list[Work]:
    works_by_authors = []
    for author in authors:
        works = Works().filter(authorships={"author": {"id": author["id"]}}).get()
        works_by_authors.extend(works)
    return works_by_authors


def get_work_institutions(works: list[Work]) -> list[Institution]:
    seen = set()
    return [
        y
        for x in works["authorships"]
        for y in x["institutions"]
        if not (y["id"] in seen or seen.add(y["id"]))
    ]


def filter_works_by_institution(
    works: list[Work], institutions: list[Institution]
) -> list[Author]:
    institution_ids = {x["id"] for x in institutions}
    result = []
    for work in works:
        work_institution_ids = {x["id"] for x in get_work_institutions(work)}
        if len(institution_ids & work_institution_ids) > 0:
            result.append(work)
    return result

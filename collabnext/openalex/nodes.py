from pyalex import Author, Institution, Work


def make_institution_nodes(institutions: list[Institution]) -> list[dict]:
    return [
        {"id": x["id"], "label": x["display_name"], "type": "INSTITUTION"}
        for x in institutions
    ]


def make_author_nodes(authors: list[Author]) -> list[dict]:
    return [
        {"id": x["id"], "label": x["display_name"], "type": "AUTHOR"} for x in authors
    ]


def make_work_nodes(works: list[Work]) -> list[dict]:
    return [
        {"id": x["id"], "label": x["title"], "type": "WORK"} for x in works
    ]
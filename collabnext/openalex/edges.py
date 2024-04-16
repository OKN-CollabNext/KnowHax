from pyalex import Author, Institution, Work


def make_associated_institution_edges(institutions: list[Institution]) -> list[dict]:
    return [
        {
            "id": f"""{x["id"]}-{y["id"]}""",
            "start": x["id"],
            "end": y["id"],
            "label": "ASSOCIATED",
            "start_type": "INSTITUTION",
            "end_type": "INSTITUTION",
        }
        for x in institutions
        for y in x["associated_institutions"]
    ]


def make_affiliated_author_edges(authors: list[Author]) -> list[dict]:
    return [
        {
            "id": f"""{x["id"]}-{y["institution"]["id"]}""",
            "start": x["id"],
            "end": y["institution"]["id"],
            "label": "AFFILIATED",
            "start_type": "AUTHOR",
            "end_type": "INSTITUTION",
        }
        for x in authors
        for y in x["affiliations"]
    ]


def make_work_author_edges(works: list[Work]) -> list[dict]:
    return [
        {
            "id": f"{work['id']}-{authorship['author']['id']}",
            "start": work['id'],
            "end": authorship['author']['id'],
            "label": "AUTHORED",
            "start_type": "WORK",
            "end_type": "AUTHOR"
        }
        for work in works
        for authorship in work.get('authorships', [])
    ]
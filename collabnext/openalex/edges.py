from pyalex import Author, Institution


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

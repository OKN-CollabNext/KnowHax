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


def make_author_institution_edges(
    authors: list[Author], institutions: list[Institution]
) -> list[dict]:
    institution_ids = [x["id"] for x in institutions]
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
        if y["institution"]["id"] in institution_ids
    ]


def make_author_work_edges(authors: list[Author], works: list[Work]) -> list[dict]:
    author_ids = [x["id"] for x in authors]
    return [
        {
            "id": f"{work['id']}-{authorship['author']['id']}",
            "start": authorship["author"]["id"],
            "end": work["id"],
            "label": "AUTHORED",
            "start_type": "WORK",
            "end_type": "AUTHOR",
        }
        for work in works
        for authorship in work.get("authorships", [])
        if authorship["author"]["id"] in author_ids
    ]


def make_work_topic_edges(works: list[Work]) -> list[dict]:
    return [
        {
            "id": f"{work['id']}-{topic['id']}",
            "start": work["id"],
            "end": topic["id"],
            "label": "TOPIC",
            "start_type": "WORK",
            "end_type": "TOPIC",
        }
        for work in works
        for topic in work["topics"]
    ]

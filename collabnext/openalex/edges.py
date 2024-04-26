from pyalex import Author, Institution, Topic, Work


def make_author_institution_edges(
    authors: list[Author], institutions: list[Institution]
) -> list[dict]:
    edges = [
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

    # Clamp authors
    author_ids = [x["id"] for x in authors]
    edges = [x for x in edges if x["start"] in author_ids]

    # Clamp institutions
    institution_ids = [x["id"] for x in institutions]
    edges = [x for x in edges if x["end"] in institution_ids]

    return edges


def make_author_work_edges(authors: list[Author], works: list[Work]) -> list[dict]:
    edges = [
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
    ]

    # Clamp authors
    author_ids = [x["id"] for x in authors]
    edges = [x for x in edges if x["start"] in author_ids]

    # Clamp works
    work_ids = [x["id"] for x in works]
    edges = [x for x in edges if x["end"] in work_ids]

    return edges


def make_work_topic_edges(works: list[Work], topics: list[Topic]) -> list[dict]:
    edges = [
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

    # Clamp works
    work_ids = [x["id"] for x in works]
    edges = [x for x in edges if x["start"] in work_ids]

    # Clamp topics
    topic_ids = [x["id"] for x in topics]
    edges = [x for x in edges if x["end"] in topic_ids]

    return edges

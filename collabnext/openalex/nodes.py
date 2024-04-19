import polars as pl
from pyalex import Author, Institution, Topic, Work

NODE_COLS = ["id", "label", "type"]


def make_institution_nodes(institutions: list[Institution]) -> pl.DataFrame:
    df = pl.DataFrame(
        [
            {"id": x["id"], "label": x["display_name"], "type": "INSTITUTION"}
            for x in institutions
        ],
    )
    df.columns = NODE_COLS
    return df


def make_author_nodes(authors: list[Author]) -> pl.DataFrame:
    df = pl.DataFrame(
        [
            {"id": x["id"], "label": x["display_name"], "type": "AUTHOR"}
            for x in authors
        ],
    )
    df.columns = NODE_COLS
    return df


def make_work_nodes(works: list[Work]) -> pl.DataFrame:
    df = pl.DataFrame(
        [{"id": x["id"], "label": x["title"], "type": "WORK"} for x in works],
    )
    df.columns = NODE_COLS
    return df


def make_topic_nodes(topics: list[Topic]) -> pl.DataFrame:
    seen = set()
    df = pl.DataFrame(
        [
            {
                "id": x["id"],
                "label": x["field"]["display_name"],
                "type": "TOPIC",
            }
            for x in topics
            # Note that topics are grouped by field
            if not (x["field"]["id"] in seen or seen.add(x["field"]["id"]))
        ],
    )
    df.columns = NODE_COLS
    return df

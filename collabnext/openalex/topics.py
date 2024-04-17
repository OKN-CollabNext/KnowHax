from pyalex import Topic, Work


def get_work_topics(works: list[Work]) -> list[Topic]:
    seen = set()
    return [
        y
        for x in works
        for y in x["topics"]
        if not (x["id"] in seen or seen.add(x["id"]))
    ]

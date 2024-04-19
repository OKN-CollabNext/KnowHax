def infer_author_topic_edges(
    author_work_edges: list[dict], work_topic_edges: list[dict]
) -> list[dict]:
    return [
        {
            "id": f"{author_work_edge['start']}-{work_topic_edge['end']}",
            "start": author_work_edge["start"],
            "end": work_topic_edge["end"],
            "label": "TOPIC",
            "start_type": "AUTHOR",
            "end_type": "TOPIC",
        }
        for author_work_edge in author_work_edges
        for work_topic_edge in work_topic_edges
        if author_work_edge["end"] == work_topic_edge["start"]
    ]

def clamp_author_nodes_to_author_edges(
    author_nodes: list[dict], author_work_edges: list[dict]
) -> list[dict]:
    author_ids = {x["start"] for x in author_work_edges}
    return [x for x in author_nodes if x["id"] in author_ids]

def clamp_author_nodes_to_edges(
    author_nodes: list[dict], edges: list[dict]
) -> list[dict]:
    author_ids = {x["start"] for x in edges}
    return [x for x in author_nodes if x["id"] in author_ids]

def clamp_author_edges_to_nodes(
    author_edges: list[dict], nodes: list[dict]
) -> list[dict]:
    author_ids = {x["id"] for x in nodes}
    return [x for x in author_edges if x["start"] in author_ids]
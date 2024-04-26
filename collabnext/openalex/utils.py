def clamp_nodes_to_edge_start(nodes: list[dict], edges: list[dict]) -> list[dict]:
    edge_ids = {x["start"] for x in edges}
    return [x for x in nodes if x["id"] in edge_ids]


def clamp_nodes_to_edge_end(nodes: list[dict], edges: list[dict]) -> list[dict]:
    edge_ids = {x["end"] for x in edges}
    return [x for x in nodes if x["id"] in edge_ids]


def clamp_edge_start_to_nodes(edges: list[dict], nodes: list[dict]) -> list[dict]:
    node_ids = {x["id"] for x in nodes}
    return [x for x in edges if x["start"] in node_ids]


def clamp_edge_end_to_nodes(edges: list[dict], nodes: list[dict]) -> list[dict]:
    node_ids = {x["id"] for x in nodes}
    return [x for x in edges if x["end"] in node_ids]

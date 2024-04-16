import json

from pyalex import Authors

from collabnext.openalex.institutions import (
    dedup_institutions,
    get_associated_institutions,
    get_institutions,
)

# Get institutions
institutions = get_institutions()

# Get associated institutions
associated_institutions = get_associated_institutions(institutions)

# Combine all unique institutions
all_institutions = dedup_institutions([*institutions, *associated_institutions])

# Create nodes
institution_nodes = [
    {"id": x["id"], "label": x["display_name"], "type": "INSTITUTION"}
    for x in all_institutions
]

# Get unique affiliated authors
seen = set()
authors = [
    y
    for x in all_institutions
    for y in Authors().filter(affiliations={"institution": {"id": x["id"]}}).get()
    if not (y["id"] in seen or seen.add(y["id"]))
]

# Get unique authors affiliated with each institution
author_nodes = [
    {"id": x["id"], "label": x["display_name"], "type": "AUTHOR"} for x in authors
]

nodes = [*institution_nodes, *author_nodes]

# Create associated institution edges
associated_institution_edges = [
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
affiliated_author_edges = [
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
edges = [*associated_institution_edges, *affiliated_author_edges]

print(json.dumps({"nodes": nodes, "edges": edges}))

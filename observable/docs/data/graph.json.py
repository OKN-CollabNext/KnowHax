import json
import os

import pyalex
from dotenv import load_dotenv
from pyalex import Authors, Institutions

# Load Secrets
load_dotenv()

# Initialize the pyalex client
pyalex.config.email = os.getenv("OPENALEX_EMAIL")

# Get 5 random institutions
institutions = [Institutions().random() for _ in range(5)]

# Gather associated institutions
associated_institutions = [
    y for x in institutions for y in x["associated_institutions"]
]

# Combine all unique institutions
seen = set()
all_institutions = [
    x
    for x in [*institutions, *associated_institutions]
    if not (x["id"] in seen or seen.add(x["id"]))
]

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

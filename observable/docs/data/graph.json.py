import json
import os

import pyalex
from dotenv import load_dotenv
from pyalex import Institutions

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

# Combine all institutions
all_institutions = [*institutions, *associated_institutions]

# Create nodes
nodes = [{"id": x["id"], "label": x["display_name"]} for x in all_institutions]

# Create associated institution edges
edges = [
    {"id": x["id"], "start": x["id"], "end": y["id"], "label": "ASSOCIATED"}
    for x in institutions
    for y in x["associated_institutions"]
]


print(json.dumps({"nodes": nodes, "edges": edges}))

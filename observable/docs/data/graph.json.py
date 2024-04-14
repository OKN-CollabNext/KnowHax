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

nodes = [{"id": x["id"], "label": x["display_name"]} for x in institutions]


# Sample data (will be replaced later with real data)
edges = [
    {"id": 1, "start": 1, "end": 2, "label": "DRAWS"},
    {"id": 2, "start": 2, "end": 3, "label": "ON"},
]

print(json.dumps({"nodes": nodes, "edges": edges}))

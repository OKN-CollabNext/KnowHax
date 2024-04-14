import json

from dotenv import load_dotenv

# Load Secrets
load_dotenv()

# Sample data (will be replaced later with real data)
nodes = [
    {"id": 1, "label": "Orb"},
    {"id": 2, "label": "Graph"},
    {"id": 3, "label": "Canvas"},
]

# Sample data (will be replaced later with real data)
edges = [
    {"id": 1, "start": 1, "end": 2, "label": "DRAWS"},
    {"id": 2, "start": 2, "end": 3, "label": "ON"},
]

print(json.dumps({"nodes": nodes, "edges": edges}))

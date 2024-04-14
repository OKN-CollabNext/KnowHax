import json

from dotenv import load_dotenv

# Load Secrets
load_dotenv()

# Sample data (will be replaced later with real data)
data = [
    {"id": 1, "label": "Orb"},
    {"id": 2, "label": "Graph"},
    {"id": 3, "label": "Canvas"},
]

print(json.dumps(data))

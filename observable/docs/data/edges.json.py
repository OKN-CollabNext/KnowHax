import json

# Sample data (will be replaced later with real data)
data = [
  { "id": 1, "start": 1, "end": 2, "label": "DRAWS" },
  { "id": 2, "start": 2, "end": 3, "label": "ON" },
]

print(json.dumps(data))
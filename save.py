import json

def save_to_json(data, path="docs/data.json"):
    with open(path, "w") as f:
        json.dump(data, f, indent=2)

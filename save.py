import json

def save_to_dashboard(results):
    with open("docs/data.json", "w") as f:
        json.dump(results, f, indent=2)

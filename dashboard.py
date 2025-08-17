import json
import os

def save_dashboard(assets):
    os.makedirs("docs", exist_ok=True)
    with open("docs/data.json", "w") as f:
        json.dump(assets, f, indent=2)

import json

def save_to_json(data, path="docs/data.json"):
    try:
        with open(path, "w") as f:
            json.dump(data, f, indent=2)
        print(f"✅ Saved {len(data)} assets to {path}")
    except Exception as e:
        print(f"❌ Failed to save data: {e}")

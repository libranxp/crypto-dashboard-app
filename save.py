import json, os

def save_to_dashboard(results):
    try:
        os.makedirs("docs", exist_ok=True)
        with open("docs/data.json", "w") as f:
            json.dump(results, f, indent=2)
        print(f"✅ Saved {len(results)} assets to dashboard.")
    except Exception as e:
        print(f"❌ Failed to save dashboard data: {e}")

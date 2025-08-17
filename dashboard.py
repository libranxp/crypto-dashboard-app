import json
import os

def save_dashboard(assets):
    try:
        os.makedirs("docs", exist_ok=True)
        with open("docs/data.json", "w") as f:
            json.dump(assets, f, indent=2)
        print("✅ Saved dashboard data to docs/data.json")
    except Exception as e:
        print(f"❌ Dashboard save failed: {e}")

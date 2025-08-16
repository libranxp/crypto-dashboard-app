import json
from modules.discovery import discover_assets
from modules.enrich import enrich_asset
from modules.alert import send_telegram_alert

def main():
    assets = discover_assets()
    enriched = []

    for asset in assets:
        try:
            data = enrich_asset(asset)
            if data.get("meets_criteria"):
                enriched.append(data)
                send_telegram_alert(data)
        except Exception as e:
            print(f"Error enriching {asset}: {e}")

    with open("docs/data.json", "w") as f:
        json.dump(enriched, f, indent=2)

if __name__ == "__main__":
    main()

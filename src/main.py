import json

from fetch_cisa import fetch_dashboard
from update_readme import update_readme


STATE_FILE = "data/state.json"


def load_state():

    with open(STATE_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def save_state(version, checked):

    state = {
        "catalogVersion": version,
        "lastChecked": checked
    }

    with open(STATE_FILE, "w", encoding="utf-8") as file:
        json.dump(state, file, indent=4)


def main():

    dashboard, catalog_version, checked = fetch_dashboard()

    state = load_state()

    if state["catalogVersion"] == catalog_version:
        print("No new CISA catalog version. Exiting.")
        return

    update_readme(dashboard)

    save_state(catalog_version, checked)

    print(f"Updated to catalog version {catalog_version}")


if __name__ == "__main__":
    main()
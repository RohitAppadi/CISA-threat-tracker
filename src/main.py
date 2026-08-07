from fetch_cisa import fetch_dashboard
from update_readme import update_readme


def main():

    dashboard = fetch_dashboard()

    update_readme(dashboard)

    print("✅ README updated successfully!")


if __name__ == "__main__":
    main()
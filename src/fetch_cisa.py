import requests
from datetime import datetime

URL = "https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json"


def fetch_dashboard():

    response = requests.get(URL)

    if response.status_code != 200:
        raise Exception(f"Failed to fetch CISA data ({response.status_code})")

    data = response.json()

    catalog_version = data["catalogVersion"]
    release_date = data["dateReleased"]
    total_vulns = data["count"]

    vulnerabilities = data["vulnerabilities"][:5]

    last_checked = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")

    dashboard = f"""
## 🛡 Live Threat Dashboard

**🕒 Last Checked:** {last_checked}

**📦 Catalog Version:** {catalog_version}

**📅 Feed Released:** {release_date}

**📊 Total Known Exploited Vulnerabilities:** {total_vulns}

**🌐 Source:** Official CISA Known Exploited Vulnerabilities (KEV) Catalog

---

| CVE | Vendor | Product | Date Added | Ransomware |
|------|--------|---------|------------|------------|
"""

    for vuln in vulnerabilities:

        status = (
            "🔴 Known"
            if vuln["knownRansomwareCampaignUse"] == "Known"
            else "🟡 Unknown"
        )

        dashboard += (
            f"| {vuln['cveID']} "
            f"| {vuln['vendorProject']} "
            f"| {vuln['product']} "
            f"| {vuln['dateAdded']} "
            f"| {status} |\n"
        )

    return dashboard, catalog_version, last_checked
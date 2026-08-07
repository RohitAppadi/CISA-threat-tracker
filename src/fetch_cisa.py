import requests

URL = "https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json"

response = requests.get(URL)
data = response.json()

vulnerabilities = data["vulnerabilities"][:5]

# Markdown table header
table = """| CVE | Vendor | Product | Date Added | Ransomware |
|-----|--------|---------|------------|------------|
"""

# Add one row per vulnerability
for vuln in vulnerabilities:
    table += (
        f"| {vuln['cveID']} "
        f"| {vuln['vendorProject']} "
        f"| {vuln['product']} "
        f"| {vuln['dateAdded']} "
        f"| {vuln['knownRansomwareCampaignUse']} |\n"
    )

print(table)
# Project Overview

## Introduction

CISA Threat Tracker is an automated threat intelligence dashboard that continuously tracks the latest entries published in the Cybersecurity and Infrastructure Security Agency (CISA) Known Exploited Vulnerabilities (KEV) Catalog.

The project retrieves vulnerability information directly from the official CISA JSON feed, processes the data, generates a structured Markdown dashboard, and updates the project's README automatically through GitHub Actions. The automation is designed to execute on a scheduled basis while minimizing unnecessary repository updates by comparing the latest catalog version against the previously processed version.

The objective of the project is to demonstrate practical cybersecurity automation using publicly available threat intelligence while applying software engineering principles such as modular design, state management, scheduled execution, and continuous integration.

---

# Problem Statement

Security teams often rely on multiple external sources to stay informed about newly exploited vulnerabilities. Although the CISA Known Exploited Vulnerabilities Catalog is publicly available, manually checking the catalog for updates is repetitive and inefficient.

The project addresses this problem by automatically monitoring the official CISA feed and presenting the latest information in a concise and readable format directly within the GitHub repository.

---

# Objectives

The primary objectives of the project are:

- Retrieve the latest vulnerability information from the official CISA KEV feed.
- Process structured JSON threat intelligence using Python.
- Generate a human-readable Markdown dashboard.
- Automatically update the project documentation.
- Automate execution through GitHub Actions.
- Prevent unnecessary commits by detecting catalog version changes.
- Demonstrate practical cybersecurity automation using open-source technologies.

---

# Key Features

- Automated retrieval of the official CISA KEV Catalog.
- Parsing of structured JSON vulnerability data.
- Markdown dashboard generation.
- Automatic README updates.
- Scheduled execution using GitHub Actions.
- Version tracking using persistent state management.
- Automatic repository updates only when new catalog versions are available.
- Modular Python codebase.

---

# Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Core application logic |
| Requests | HTTP communication with the CISA API |
| JSON | Threat intelligence data format |
| Markdown | Dashboard generation |
| GitHub Actions | Workflow automation |
| Git | Version control |
| GitHub | Repository hosting and CI platform |

---

# Data Source

The project retrieves vulnerability information from the official CISA Known Exploited Vulnerabilities Catalog.

Information extracted from the feed includes:

- Catalog Version
- Release Date
- Total Vulnerability Count
- CVE Identifier
- Vendor
- Product
- Date Added
- Known Ransomware Campaign Status

The project intentionally limits the displayed information to the latest vulnerabilities in order to provide a concise dashboard while maintaining readability.

---

# Workflow

The project follows the workflow below.

```

GitHub Actions
│
▼
Execute main.py
│
▼
Retrieve KEV JSON Feed
│
▼
Parse Vulnerability Data
│
▼
Compare Catalog Version
│
├───────────────┐
│ │
No Changes New Version
│ │
▼ ▼
Exit Generate Dashboard
│
▼
Update README
│
▼
Update State
│
▼
Commit Changes
│
▼
Push Repository

```

---

# Repository Output

The generated dashboard contains:

- Current catalog version
- Feed release date
- Total number of known exploited vulnerabilities
- Latest vulnerabilities published by CISA
- Ransomware campaign status

The dashboard is regenerated only when a newer catalog version becomes available.

---

# Design Philosophy

The project was designed with the following principles:

- Simplicity
- Maintainability
- Modularity
- Automation
- Reproducibility

Rather than implementing unnecessary features, the project focuses on solving a single problem efficiently while remaining easy to understand and extend.

---

# Limitations

Current limitations include:

- The dashboard displays only a subset of the available vulnerability information.
- Historical vulnerability trends are not stored.
- The project currently monitors only the CISA KEV Catalog.
- No database is used for long-term storage.

---

# Future Enhancements

Potential future improvements include:

- Integration with the National Vulnerability Database (NVD).
- CVSS score visualization.
- EPSS probability integration.
- Vendor-specific filtering.
- Historical vulnerability tracking.
- HTML dashboard generation.
- GitHub Pages deployment.
- Interactive web interface.

---

# Conclusion

CISA Threat Tracker demonstrates the practical application of cybersecurity automation using publicly available threat intelligence. The project combines Python, REST APIs, GitHub Actions, Markdown generation, and version control into a maintainable automation pipeline capable of monitoring and presenting real-world security information with minimal manual intervention.
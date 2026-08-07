# Architecture

## Overview

CISA Threat Tracker follows a modular architecture in which each component is responsible for a single task. Rather than implementing all functionality inside a single script, the project separates data acquisition, dashboard generation, state management, and workflow automation into independent modules.

This separation improves maintainability, readability, and future extensibility.

---

# Project Structure

```
CISA-Threat-Tracker/
│
├── .github/
│   └── workflows/
│       └── update-threat-feed.yml
│
├── data/
│   └── state.json
│
├── docs/
│   ├── PROJECT_OVERVIEW.md
│   ├── ARCHITECTURE.md
│   ├── ENGINEERING_JOURNAL.md
│   └── LEARNINGS.md
│
├── src/
│   ├── fetch_cisa.py
│   ├── update_readme.py
│   └── main.py
│
├── README.md
├── requirements.txt
├── .gitignore
└── LICENSE
```

---

# Component Overview

The project is divided into four logical components.

```
GitHub Actions
        │
        ▼
Application Entry Point
        │
        ▼
Threat Intelligence Retrieval
        │
        ▼
Dashboard Generation
        │
        ▼
README Update
        │
        ▼
State Management
```

Each component performs a single responsibility.

---

# Directory Structure

## .github/

Contains the GitHub Actions workflow responsible for scheduling and executing the automation.

Responsibilities include:

- Repository checkout
- Python environment creation
- Dependency installation
- Script execution
- Automatic commits
- Repository updates

---

## data/

Contains persistent application state.

Current file:

```
state.json
```

Purpose:

Stores metadata about the previously processed CISA catalog.

Example:

```json
{
    "catalogVersion": "2026.08.07",
    "lastChecked": "2026-08-08 01:10 UTC"
}
```

The application compares this value against the latest API response to determine whether a repository update is required.

---

## docs/

Contains project documentation.

Documentation is intentionally separated from the source code to improve maintainability and allow users to understand the project without examining implementation details.

---

## src/

Contains the application source code.

The application is intentionally modular.

---

# Source Code Modules

## main.py

Purpose

Acts as the application entry point.

Responsibilities

- Load stored application state.
- Execute the CISA data retrieval module.
- Compare catalog versions.
- Determine whether an update is required.
- Trigger README generation.
- Save the updated application state.

main.py contains the application's primary decision-making logic.

---

## fetch_cisa.py

Purpose

Responsible for retrieving and processing threat intelligence.

Responsibilities

- Connect to the official CISA KEV endpoint.
- Validate the HTTP response.
- Parse JSON data.
- Extract relevant vulnerability fields.
- Generate a Markdown dashboard.
- Return processed information to the application.

Inputs

Official CISA JSON feed.

Outputs

- Markdown dashboard
- Catalog version
- Timestamp

---

## update_readme.py

Purpose

Updates the project README while preserving all existing documentation.

Responsibilities

- Open README.md
- Locate predefined markers
- Replace only the dashboard section
- Preserve all remaining content
- Write the updated file

The module performs targeted replacement rather than rewriting the entire document.

---

# README Update Strategy

The project uses marker-based replacement.

Markers:

```html
<!-- THREAT-FEED:START -->

Dashboard Content

<!-- THREAT-FEED:END -->
```

Only the content between these markers is replaced.

Advantages

- Existing documentation remains untouched.
- No manual editing is required.
- Easy to extend with additional generated sections.

---

# State Management

The application maintains a lightweight state file.

Workflow

```
Read state.json
        │
        ▼
Retrieve latest catalog version
        │
        ▼
Compare versions
        │
        ├───────────────┐
        │               │
Same Version     New Version
        │               │
        ▼               ▼
Terminate      Continue Update
```

This approach prevents unnecessary repository updates.

---

# Dashboard Generation

The dashboard is generated dynamically during execution.

Displayed information includes:

- Catalog version
- Feed release date
- Total vulnerability count
- Latest published vulnerabilities
- Vendor information
- Product information
- Ransomware campaign status

The generated Markdown is inserted directly into README.md.

---

# GitHub Actions Workflow

The automation executes according to the following sequence.

```
Workflow Trigger
        │
        ▼
Checkout Repository
        │
        ▼
Install Python
        │
        ▼
Install Dependencies
        │
        ▼
Execute main.py
        │
        ▼
Generate Dashboard
        │
        ▼
Compare State
        │
        ▼
Update README
        │
        ▼
Commit Changes
        │
        ▼
Push Repository
```

The workflow may be executed manually or through the scheduled cron trigger.

---

# Data Flow

The following diagram illustrates how information moves through the application.

```
Official CISA API
        │
        ▼
HTTP Request
        │
        ▼
JSON Response
        │
        ▼
Python Dictionary
        │
        ▼
Data Processing
        │
        ▼
Markdown Dashboard
        │
        ▼
README Update
        │
        ▼
Git Commit
        │
        ▼
GitHub Repository
```

---

# Design Decisions

The project follows several software engineering principles.

## Single Responsibility

Each module performs one clearly defined task.

---

## Separation of Concerns

Data retrieval, state management, dashboard generation, and repository updates remain independent.

---

## Idempotent Execution

Repeated executions without new catalog versions do not produce unnecessary repository updates.

---

## Maintainability

The modular design allows additional threat intelligence feeds to be integrated with minimal modification.

---

# Extension Strategy

Future integrations may include:

- National Vulnerability Database (NVD)
- EPSS
- CVSS
- GitHub Security Advisories
- CISA Alerts
- HTML report generation
- GitHub Pages dashboard

The existing architecture allows additional data sources to be incorporated without requiring significant changes to the application's structure.

---

# Summary

CISA Threat Tracker follows a modular automation architecture that separates data retrieval, processing, presentation, and workflow execution into independent components. This design improves readability, simplifies maintenance, and provides a scalable foundation for future threat intelligence integrations.
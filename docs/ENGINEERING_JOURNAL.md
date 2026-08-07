# Engineering Journal

## Purpose

This document records the engineering process followed during the development of CISA Threat Tracker. Rather than serving as a changelog, it documents the reasoning behind major implementation decisions, architectural improvements, problems encountered during development, and the solutions adopted.

The goal is to provide future contributors with context regarding why the project evolved into its current architecture.

---

# Initial Objective

The original objective was straightforward.

Develop a Python application capable of retrieving the latest entries from the CISA Known Exploited Vulnerabilities (KEV) Catalog and displaying them within a GitHub repository.

The initial implementation consisted of a single Python script responsible for requesting data from the CISA API and printing the response to the terminal.

At this stage the project contained no automation, documentation, or modular structure.

---

# Phase 1 — API Integration

The first milestone was successfully connecting to the official CISA Known Exploited Vulnerabilities feed.

The application used the Requests library to perform an HTTP GET request against the public JSON endpoint.

Initial goals included:

- Verify API accessibility
- Validate HTTP responses
- Understand the JSON structure
- Extract vulnerability information

After retrieving the response, the JSON payload was inspected to identify useful fields.

The following fields were selected for the dashboard:

- catalogVersion
- dateReleased
- count
- vulnerabilities

Each vulnerability entry contained several attributes, including:

- CVE Identifier
- Vendor
- Product
- Date Added
- Known Ransomware Campaign Status

These fields were considered sufficient to produce a concise operational dashboard.

---

# Phase 2 — Dashboard Generation

Once the data retrieval process was complete, attention shifted toward presentation.

Instead of printing raw dictionaries to the console, the application generated a Markdown table dynamically.

This decision allowed GitHub itself to function as the dashboard interface without requiring additional frontend development.

Advantages included:

- Zero deployment complexity
- Native GitHub rendering
- Easy portability
- Human-readable output

---

# Phase 3 — README Automation

The initial implementation rewrote the entire README file during every execution.

Although functional, this approach introduced two significant problems.

1. Existing documentation could be overwritten.
2. Manual edits would be lost after each execution.

To solve this issue, a marker-based replacement strategy was introduced.

Special markers were embedded inside the README.

```html
<!-- THREAT-FEED:START -->

Generated Content

<!-- THREAT-FEED:END -->
```

Only the content between these markers is modified.

Everything outside the markers remains untouched.

This significantly reduced the risk of accidental data loss while simplifying future extensions.

---

# Phase 4 — Project Modularization

As functionality increased, the original single-file implementation became increasingly difficult to maintain.

The project was refactored into three independent modules.

```
fetch_cisa.py

update_readme.py

main.py
```

Responsibilities were divided according to the Single Responsibility Principle.

fetch_cisa.py

Responsible for:

- API communication
- JSON processing
- Dashboard generation

update_readme.py

Responsible for:

- Reading README.md
- Marker detection
- Markdown replacement
- File writing

main.py

Responsible for:

- Workflow orchestration
- State management
- Decision making

This separation improved readability while making future modifications significantly easier.

---

# Phase 5 — GitHub Actions

One of the primary project objectives was to eliminate manual execution.

GitHub Actions was selected as the automation platform because it provides:

- Cloud-hosted runners
- Native GitHub integration
- Scheduled execution
- Repository write access

The workflow performs the following tasks:

1. Checkout repository
2. Install Python
3. Install dependencies
4. Execute the application
5. Commit generated changes
6. Push updates back to the repository

This transformed the project from a local script into a continuously running automation pipeline.

---

# Phase 6 — State Management

A major design challenge emerged after the automation was completed.

The workflow successfully updated the README during every execution.

However, many executions produced identical dashboards because the CISA catalog had not changed.

This resulted in unnecessary commits.

To solve this issue, lightweight state management was introduced.

The application stores the previously processed catalog version inside:

```
data/state.json
```

Before generating a new dashboard, the application compares the latest catalog version against the stored value.

If both versions match, execution terminates without updating the repository.

This ensures that repository history reflects meaningful updates rather than scheduled executions.

---

# Technical Challenges

## Understanding GitHub Actions

Initially, GitHub Actions was unfamiliar.

Understanding the lifecycle of workflow runners required learning that each execution occurs inside a temporary virtual machine with no persistent local state.

This influenced dependency installation and repository checkout strategy.

---

## Dependency Management

The first workflow execution failed because required Python packages were unavailable inside the runner.

The solution was to introduce a requirements.txt file and install dependencies during every workflow execution.

This guarantees reproducible environments.

---

## JSON Processing

Understanding the structure of nested dictionaries and lists required careful inspection of the API response.

Early mistakes included attempting to access list elements as dictionary keys.

Once the response structure was understood, extracting vulnerability fields became straightforward.

---

## README Modification

Directly overwriting README.md initially removed manually written documentation.

The marker-based replacement strategy resolved this problem while allowing generated and manually written content to coexist.

---

## Repository Permissions

The workflow initially lacked permission to push commits.

Repository permissions were updated to allow GitHub Actions write access.

Once configured, automated commits became possible without requiring personal access tokens.

---

## State Tracking

Preventing unnecessary commits required introducing persistent application state.

A lightweight JSON file was selected instead of a database because the project stores only a small amount of metadata.

This solution remains simple while supporting future extensions.

---

# Design Decisions

Several architectural decisions influenced the final implementation.

## Modular Design

The application separates concerns into independent modules rather than combining all functionality inside a single script.

This improves maintainability and simplifies testing.

---

## Markdown as the Presentation Layer

Rather than building a web interface, GitHub's native Markdown renderer serves as the dashboard.

This eliminates deployment overhead while maintaining excellent readability.

---

## Scheduled Automation

Using GitHub Actions removes the dependency on a continuously running local machine.

Automation occurs entirely within GitHub's infrastructure.

---

## Lightweight State Storage

Persistent metadata is stored using JSON instead of a relational database.

The project's requirements do not justify additional infrastructure complexity.

---

# Lessons Learned

The project provided practical experience with:

- REST APIs
- HTTP communication
- JSON processing
- Python file handling
- Markdown generation
- GitHub Actions
- Continuous Integration
- Repository automation
- State management
- Modular software architecture
- Automation design principles

---

# Future Engineering Improvements

Possible future enhancements include:

- Structured logging
- Unit testing
- Exception logging
- Dashboard version history
- Historical vulnerability tracking
- Integration with additional threat intelligence feeds
- HTML report generation
- GitHub Pages deployment

These enhancements can be incorporated without major architectural changes due to the modular design adopted during development.

---

# Conclusion

CISA Threat Tracker evolved from a simple API consumption script into an automated threat intelligence pipeline.

Throughout development, emphasis was placed on maintainability, modularity, reproducibility, and automation rather than feature quantity.

The final architecture demonstrates how relatively small Python applications can leverage publicly available threat intelligence together with GitHub Actions to create practical cybersecurity automation capable of operating without manual intervention.
START_MARKER = "<!-- THREAT-FEED:START -->"
END_MARKER = "<!-- THREAT-FEED:END -->"


def update_readme(dashboard):

    with open("README.md", "r", encoding="utf-8") as file:
        content = file.read()

    start = content.find(START_MARKER)
    end = content.find(END_MARKER)

    if start == -1 or end == -1:
        raise Exception("README markers not found!")

    new_content = (
        content[: start + len(START_MARKER)]
        + "\n\n"
        + dashboard
        + "\n"
        + content[end:]
    )

    with open("README.md", "w", encoding="utf-8") as file:
        file.write(new_content)
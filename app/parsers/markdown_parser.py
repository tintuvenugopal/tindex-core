from pathlib import Path


class MarkdownParser:
    """
    Very first deterministic parser.

    Converts a markdown knowledge document into
    simple key/value sections.
    """

    def parse(self, filename: str) -> dict:
        lines = Path(filename).read_text().splitlines()

        data = {}
        section = None

        for line in lines:
            line = line.strip()

            if not line:
                continue

            if line.startswith("# "):
                data["title"] = line[2:].strip()
                continue

            if line.startswith("## "):
                section = line[3:].strip()
                data[section] = {}
                continue

            if ":" in line and section:
                key, value = line.split(":", 1)
                data[section][key.strip()] = value.strip()

        return data
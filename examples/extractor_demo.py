from app.extractors.canonical_extractor import CanonicalExtractor
from app.parsers.markdown_parser import MarkdownParser


def main():
    parser = MarkdownParser()
    extractor = CanonicalExtractor()

    parsed = parser.parse("knowledge/sample/apple.md")

    canonical = extractor.extract(parsed)

    print("\n===== ENTITY =====")
    print(canonical["entity"])

    print("\n===== PROPERTY =====")
    print(canonical["property"])

    print("\n===== OBSERVATION =====")
    print(canonical["observation"])


if __name__ == "__main__":
    main()
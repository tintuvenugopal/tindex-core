from app.parsers.markdown_parser import MarkdownParser


def main():
    parser = MarkdownParser()

    document = parser.parse(
        "knowledge/sample/apple.md"
    )

    print(document)


if __name__ == "__main__":
    main()
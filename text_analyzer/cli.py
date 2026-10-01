import argparse
from pathlib import Path

from text_analyzer.analyzer import analyze_text


def format_report(results):
    """Format analysis results as a readable report."""
    lines = [
        "Text Analysis Report",
        "--------------------",
        f"Characters: {results['characters']}",
        f"Words: {results['words']}",
        f"Sentences: {results['sentences']}",
        f"Paragraphs: {results['paragraphs']}",
        f"Unique words: {results['unique_words']}",
        f"Average word length: {results['average_word_length']:.2f}",
        f"Readability score: {results['readability_score']:.2f}",
        "",
        "Most common words:",
    ]

    for word, count in results["most_common_words"]:
        lines.append(f"{word}: {count}")

    return "\n".join(lines)


def main():
    """Run the command-line text analyzer."""
    parser = argparse.ArgumentParser(
        description="Analyze a text file."
    )
    parser.add_argument("file", help="Path to a .txt file")
    args = parser.parse_args()

    file_path = Path(args.file)

    if not file_path.exists():
        print(f"Error: File '{args.file}' was not found.")
        return

    if not file_path.is_file():
        print(f"Error: '{args.file}' is not a file.")
        return

    try:
        text = file_path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        print(f"Error: File '{args.file}' is not a valid UTF-8 text file.")
        return
    except OSError as error:
        print(f"Error: Could not read '{args.file}': {error}")
        return

    results = analyze_text(text)
    print(format_report(results))


if __name__ == "__main__":
    main()
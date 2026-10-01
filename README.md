# Text Analyzer

A small Python command-line tool that analyzes a text file and reports basic text statistics, including word count, sentence count, paragraph count, unique words, common words, average word length, and an approximate readability score.

## Features

- Count characters, words, sentences, and paragraphs
- Count unique words
- Find the most common words
- Calculate average word length
- Calculate an approximate Flesch Reading Ease score
- Handle missing files and invalid file paths without crashing
- Read UTF-8 text files
- Run from the command line

## Project Structure

```text
text-analyzer/
├── text_analyzer/
│   ├── __init__.py
│   ├── analyzer.py
│   └── cli.py
├── tests/
│   ├── __init__.py
│   └── test_analyzer.py
├── docs/
│   ├── ms1418_architect.txt
│   ├── plan.md
│   └── transcripts/
│       └── ms1418_architect.txt
├── sample.txt
├── main.py
├── README.md
├── requirements.txt
├── pyproject.toml
└── .gitignore
```

## File Responsibilities

- `text_analyzer/analyzer.py` contains the text analysis functions.
- `text_analyzer/cli.py` handles command-line arguments, file reading, error handling, and report formatting.
- `main.py` provides the main entry point for running the application.
- `tests/test_analyzer.py` contains automated tests for the analysis functions.
- `sample.txt` provides a sample input file for manual testing.
- `docs/plan.md` contains the project implementation plan.
- `docs/ms1418_architect.txt` and `docs/transcripts/ms1418_architect.txt` contain the Architect-stage documentation and transcript.

## Requirements

- Python 3.9 or later
- pytest
- Ruff

The core text analysis uses only Python standard-library modules.

## Installation

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the project dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the analyzer by providing a text file:

```bash
python main.py sample.txt
```

The program prints a report similar to:

```text
Text Analysis Report
--------------------
Characters: ...
Words: ...
Sentences: ...
Paragraphs: ...
Unique words: ...
Average word length: ...
Readability score: ...

Most common words:
...
```

You can also provide another text file:

```bash
python main.py myfile.txt
```

## Invalid File Handling

If the file does not exist, the program displays an error message instead of crashing:

```bash
python main.py missing.txt
```

Example:

```text
Error: File 'missing.txt' was not found.
```

The program also checks that the provided path is a file and handles invalid UTF-8 files and other file-reading errors.

## Testing

The project uses pytest for automated testing.

Run the full test suite with:

```bash
pytest
```

The tests cover normal cases and edge cases such as:

- Empty text
- Punctuation
- Multiple blank lines
- Repeated words
- Average word length for empty text
- Readability for empty text
- Combined analysis results

## Code Quality

Ruff is used to check the Python code for common errors and formatting issues.

Run Ruff with:

```bash
ruff check .
```

## Design Decisions and Limitations

The project intentionally keeps text analysis simple and dependency-light.

- Words are normalized to lowercase.
- Sentence counting uses `.`, `!`, and `?` as sentence-ending punctuation.
- Paragraphs are separated by blank lines.
- Syllable counts are estimated using a simple rule-based approach.
- The readability score is an approximate Flesch Reading Ease score.
- The tool currently analyzes one UTF-8 text file at a time.

The project does not include a graphical interface, database, external API, machine-learning model, advanced NLP processing, or support for PDF and Word documents.

## AI-Assisted Development

This project was developed using an AI-assisted workflow with separate Architect, Builder, Tester, and Reviewer stages.

The Architect stage was used to define the project scope, structure, requirements, and implementation plan. The Builder stage was used to implement the planned structure and functionality. Automated tests and Ruff were then used to verify the implementation and code quality.
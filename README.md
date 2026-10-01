# Text Analyzer
[![Tests](https://github.com/MasomaSh/text-analyzer/actions/workflows/tests.yml/badge.svg)](https://github.com/MasomaSh/text-analyzer/actions/workflows/tests.yml)
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
│   ├── plan.md
│   └── transcripts/
│       ├── ms1418_architect.txt
│       ├── ms1418_builder.txt
│       └── ms1418_tester.txt
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
- `docs/plan.md` contains the finalized project implementation plan.
- `docs/transcripts/ms1418_architect.txt` contains the Architect-stage conversation.
- `docs/transcripts/ms1418_builder.txt` contains the Builder-stage conversation.
- `docs/transcripts/ms1418_tester.txt` contains the Tester-stage conversation.

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

The test suite contains 18 tests covering normal behavior and edge cases, including:

- Empty text
- Whitespace-only text
- Punctuation-only text
- Repeated words
- Case-insensitive word counting
- Apostrophes
- Multiple sentence-ending punctuation
- Multiple blank lines
- Average word length for empty text
- Readability for empty text
- Combined analysis results

The final test suite passed all 18 tests.

## Code Quality

Ruff is used to check the Python code for common errors and code quality issues.

Run Ruff with:

```bash
ruff check .
```

The final Ruff check reported no issues.

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

This project was developed using a structured AI-assisted workflow with separate Architect, Builder, and Tester roles.

### Architect

The Architect stage examined the project requirements and created the implementation plan in `docs/plan.md`. The plan defined the project structure, analysis functions, command-line behavior, testing requirements, edge cases, and scope limitations.

### Builder

The Builder stage used the finalized Architect plan to implement the project. The Builder created the Python package, command-line interface, automated tests, sample input, configuration files, and project documentation.

I reviewed the generated implementation and made corrections where necessary before continuing to the testing stage.

### Manual Smoke Test

Before the Tester stage, I manually verified that the project could be set up and run successfully. I followed the documented installation instructions, created and activated the virtual environment, installed the dependencies, and ran the application with a sample text file.

### Tester

The Tester stage independently reviewed the implementation against `docs/plan.md`, inspected and ran the test suite, checked typical and edge-case behavior, and reviewed the setup and usage instructions.

The Tester identified additional edge cases that should be tested. After reviewing those recommendations, I expanded the test suite from 13 tests to 18 tests and corrected a missing `extract_words` import when the new apostrophe test initially failed.

## Manual Smoke Test

The project was manually tested after implementation and before the Tester stage.

The documented setup instructions were followed by creating and activating the virtual environment and installing the required dependencies from `requirements.txt`.

The main feature was tested with:

```bash
python main.py sample.txt
```

The program started successfully and produced the expected text analysis report, including:

- Character count
- Word count
- Sentence count
- Paragraph count
- Unique word count
- Average word length
- Readability score
- Most common words

Invalid file handling was also tested with:

```bash
python main.py missing.txt
```

The program returned an error message indicating that the file was not found and did not produce a traceback.

The project does not use containers, so no container build or runtime test was required.

## Evaluate and Reflect

### Selected Option

Option 3 was selected for this project: Create a New Project.

### Project Purpose

The purpose of this project is to build a small command-line text analyzer that calculates basic text statistics from a text file. The project was intentionally kept simple and uses Python's standard library for the core analysis.

### AI Recommendation Accepted

One recommendation I accepted was to add edge-case tests for whitespace-only text, punctuation-only text, apostrophes, case-insensitive word counting, and multiple sentence-ending punctuation.

These tests helped verify behavior beyond the basic examples and increased the test suite from 13 tests to 18 tests.

### AI Recommendation Changed or Rejected

One recommendation I changed was the testing workflow. Instead of relying only on the existing test suite, I reviewed the test file myself and added additional cases based on the project requirements.

During this process, the new apostrophe test initially revealed a missing `extract_words` import. I corrected the import and reran the tests to verify the fix.

### Independent Verification

I independently verified the final project by:

1. Following the documented setup instructions.
2. Creating and activating the virtual environment.
3. Installing the dependencies from `requirements.txt`.
4. Running the application with the valid `sample.txt` file.
5. Running the application with a missing file to verify error handling.
6. Running the complete pytest test suite.
7. Running Ruff to check code quality.

The final test suite passed all 18 tests, and Ruff reported no issues.
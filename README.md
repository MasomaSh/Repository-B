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

## Manual Smoke Test

The project was manually tested after implementation.

The documented setup instructions were followed by creating and activating the virtual environment and installing the required dependencies from `requirements.txt`.

The main feature was tested with:

```bash
python main.py sample.txt
```

The program started successfully and produced the expected text analysis report, including character count, word count, sentence count, paragraph count, unique word count, average word length, readability score, and most common words.

Invalid file handling was also tested with:

```bash
python main.py missing.txt
```

The program returned an error message indicating that the file was not found and did not produce a traceback.

The project does not use containers, so no container build or runtime test was required.

## Evaluate and Reflect

### Selected Option

Option 3 was selected for this project.

### Project Purpose

The purpose of this project is to build a small command-line text analyzer that calculates basic text statistics from a text file. The project was intentionally kept simple and uses Python's standard library for the core analysis.

### AI-Assisted Workflow

The Architect role was used to examine the project requirements and create the implementation plan in `docs/plan.md`. The plan defined the project structure, analysis functions, CLI behavior, testing requirements, and scope limitations.

The Builder role implemented the architecture by creating the Python package, CLI, tests, sample input, configuration files, documentation, and supporting project files.

The Tester role independently reviewed the implementation against the planned requirements and focused on additional edge cases. The test suite was expanded from 13 tests to 18 tests.

### AI Recommendation Accepted

One recommendation I accepted was to add edge-case tests for whitespace-only text, punctuation-only text, apostrophes, case-insensitive word counting, and multiple sentence-ending punctuation. These tests helped verify behavior beyond the basic examples.

### AI Recommendation Changed or Rejected

One recommendation I changed was the testing workflow. Instead of relying only on the existing test suite, I reviewed the test file myself and added additional cases based on the project requirements. I also corrected a missing `extract_words` import when the new apostrophe test initially failed.

### Independent Verification

I independently verified the final project by running the application from the command line with both a valid sample file and a missing file. I also ran the complete pytest suite and Ruff checks. The final test suite passed all 18 tests, and Ruff reported no issues.
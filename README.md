# Text Analyzer
[![Tests](https://github.com/MasomaSh/text-analyzer/actions/workflows/tests.yml/badge.svg)](https://github.com/MasomaSh/text-analyzer/actions/workflows/tests.yml)

A small Python command-line text analyzer that reads a UTF-8 text file and reports basic text statistics and readability information.

## Features

The analyzer reports:

- Number of characters
- Number of words
- Number of sentences
- Number of paragraphs
- Number of unique words
- Most common words
- Average word length
- Approximate Flesch Reading Ease score
- Clear error handling for missing or invalid files

The project uses Python's standard library for the core text analysis functionality.

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

- `text_analyzer/analyzer.py` contains the main text analysis functions.
- `text_analyzer/cli.py` handles the command-line interface and file input.
- `main.py` provides the main entry point for running the application.
- `tests/test_analyzer.py` contains the automated test suite.
- `docs/plan.md` contains the implementation plan created during the Architect stage.
- `docs/transcripts/` contains the visible AI conversation transcripts from the Architect, Builder, and Tester stages.

## Requirements

- Python 3.9+
- pytest
- Ruff

## Installation

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

## Usage

Run the analyzer by providing a text file:

```bash
python main.py sample.txt
```

The program prints a report containing the text statistics and readability information.

### Invalid File Handling

If the specified file does not exist, the program displays a clear error message instead of producing a Python traceback.

Example:

```bash
python main.py missing.txt
```

## Testing

The project uses `pytest` for automated testing.

Run the full test suite with:

```bash
pytest -v
```

The final test suite contains **18 tests** covering both typical inputs and edge cases.

Tests include:

- Empty text
- Whitespace-only text
- Punctuation-only text
- Repeated words
- Case-insensitive word counting
- Words containing apostrophes
- Multiple sentence-ending punctuation marks
- Multiple blank lines
- Empty-text average word length
- Empty-text readability
- Combined analysis results
- File and input handling

All 18 tests passed during final verification.

## Code Quality

Ruff is used for Python linting.

Run Ruff with:

```bash
ruff check .
```

The final Ruff check reported no issues.

## Continuous Integration

GitHub Actions automatically runs checks when changes are pushed or a pull request is opened.

The workflow:

1. Checks out the repository.
2. Sets up Python 3.11.
3. Installs the project dependencies.
4. Checks Python syntax.
5. Runs Ruff.
6. Runs the full pytest test suite.

The workflow is defined in:

```text
.github/workflows/tests.yml
```

The status badge at the top of this README shows the current CI status.

## Manual Smoke Test

Before the Tester stage, I manually verified the application by following the setup instructions and running the main functionality.

The smoke test included:

1. Creating and activating a virtual environment.
2. Installing the required packages.
3. Running the analyzer on `sample.txt`.
4. Checking that the expected analysis report was produced.
5. Running the analyzer with a missing file.
6. Checking that the program returned a clear file-not-found error without a traceback.

No containers were required for this project.

## AI-Assisted Development

The project was completed using three separate AI-assisted development roles: Architect, Builder, and Tester.

Each role was completed in a separate AI conversation.

### 1. Architect

The Architect stage examined the project requirements, proposed the project structure and implementation approach, identified risks and testing requirements, and created the implementation plan in:

```text
docs/plan.md
```

The plan defined the analysis functions, command-line behavior, testing requirements, edge cases, and project scope.

I reviewed the plan before implementation and made any necessary corrections before providing it to the Builder.

### 2. Builder

The Builder received the Architect plan and implemented the project.

The Builder created and updated the application files, tests, and documentation according to the plan.

After the Builder stage, I reviewed the generated code and made my own corrections where needed.

### 3. Manual Smoke Test

Before using the Tester role, I independently ran the application myself.

I verified that:

- The installation instructions worked.
- The program started successfully.
- The main text analysis functionality worked.
- The output was produced as expected.
- Missing-file handling worked without a traceback.

The smoke test was completed before the Tester conversation.

### 4. Tester

The Tester independently reviewed the implementation against `docs/plan.md`, inspected the tests, considered typical and edge-case inputs, and checked the setup instructions.

The Tester identified additional edge cases that were not initially covered.

Based on the Tester recommendations, I expanded the test suite from 13 tests to 18 tests.

One issue was also found during testing with the apostrophe test because `extract_words` was not imported correctly. I corrected the issue and reran the tests.

The final result was:

```text
18 passed
```

Ruff was also run again after the corrections and reported no issues.

## AI Conversation Transcripts

The project includes the visible conversation transcripts from the three AI roles used during development:

- `docs/transcripts/ms1418_architect.txt`
- `docs/transcripts/ms1418_builder.txt`
- `docs/transcripts/ms1418_tester.txt`

Each transcript preserves the visible conversation for its respective role, including:

- My prompts
- AI responses
- Follow-up questions
- Corrections
- The final visible result or summary

The transcripts were saved as plain-text files and were not rewritten or shortened.

Private information, if present, was removed or replaced with `[REDACTED]`.

The three roles were completed in separate AI conversations:

1. Architect
2. Builder
3. Tester

Only conversation content visible to me is included. No hidden AI reasoning or internal chain of thought is included.

## Evaluate and Reflect

### Selected Option

**Option 3: Create a New Project**

I selected the option to create a new project rather than modify an existing project.

### Project Purpose

The purpose of the project is to create a simple command-line text analyzer that demonstrates Python development, testing, code quality, error handling, and an AI-assisted development workflow.

### AI Recommendation Accepted

I accepted the Architect's recommendation to separate the project into analysis and command-line interface components. This made the text analysis functions easier to test independently from file and command-line handling.

I also accepted the Tester's recommendation to expand the test suite with additional edge cases.

### AI Recommendation Changed or Rejected

The AI recommendations were not followed without review. Where recommendations did not fit the project's scope or requirements, I made the final decisions and adjusted the implementation accordingly.

For example, the project intentionally keeps the readability calculation approximate rather than adding a larger external NLP or readability library. This keeps the project small and focused on the required functionality.

### Independent Verification

I independently verified the final project after the AI-assisted development stages by:

- Running the application manually with a valid input file.
- Testing missing-file behavior.
- Running all 18 automated tests.
- Running Ruff.
- Reviewing the project structure and README.
- Confirming that the CI workflow was configured to run syntax checks, linting, and tests.

The final verification completed successfully with **18 passing tests** and no Ruff issues.
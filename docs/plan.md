# Architect Stage — Text Analyzer

## 1. Project Overview

### Project Goal

The goal of this project is to build a small Python command-line Text Analyzer that accepts a `.txt` file and generates a basic text analysis report.

The project is designed to demonstrate an AI-assisted development workflow while remaining simple enough to understand, test, and maintain.

The application will use only Python's standard library for its core functionality. `pytest` will be used for testing and Ruff will be used for code quality checks.

### Core Requirements

The program should:

- Accept a `.txt` file as input.
- Read the contents of the file.
- Calculate the number of characters.
- Calculate the number of words.
- Calculate the number of sentences.
- Calculate the number of paragraphs.
- Calculate the number of unique words.
- Identify the most common words.
- Calculate average word length.
- Calculate a basic readability measure.
- Display the results in a readable command-line report.
- Handle common invalid inputs without crashing.
- Include automated tests.
- Pass Ruff code-quality checks.

The project will not use an external dataset, database, API, or external NLP library.

---

## 2. Proposed Project Structure

The proposed repository structure is:

```text
text-analyzer/
│
├── text_analyzer/
│   ├── __init__.py
│   ├── analyzer.py
│   └── cli.py
│
├── tests/
│   ├── __init__.py
│   └── test_analyzer.py
│
├── sample.txt
├── main.py
├── README.md
├── requirements.txt
├── pyproject.toml
└── .gitignore
```

### File Responsibilities

**`main.py`**

Provides the main entry point for running the application.

**`text_analyzer/analyzer.py`**

Contains the core text-analysis functions. This module should not be responsible for command-line input or output.

**`text_analyzer/cli.py`**

Handles command-line interaction, including receiving the file path, reading the file, displaying the report, and handling user-facing errors.

**`tests/test_analyzer.py`**

Contains pytest tests for the analysis functions and selected command-line behavior.

**`sample.txt`**

Provides a small text file for manual testing and demonstration.

**`README.md`**

Documents the project, installation, usage, testing, design decisions, limitations, and AI-assisted development process.

**`requirements.txt`**

Lists the testing dependency, primarily `pytest`. Ruff may also be included depending on the project's chosen setup.

**`pyproject.toml`**

Stores project configuration, including Ruff configuration and potentially pytest configuration.

**`.gitignore`**

Prevents unnecessary files such as Python cache files and virtual environments from being committed.

---

## 3. Proposed Application Design

The application will separate text-analysis logic from command-line interaction.

The basic flow will be:

```text
Text File
   ↓
Command-Line Interface
   ↓
Read Text
   ↓
Text Analysis Functions
   ↓
Analysis Results
   ↓
Formatted Report
```

The CLI should call the analysis module rather than performing the calculations itself.

This separation will make the project easier to test and maintain.

---

## 4. Proposed Functions

The analysis module will contain small functions with individual responsibilities.

### `count_characters(text)`

Counts the characters in the input text.

For this project, spaces and newline characters will be included in the character count.

### `extract_words(text)`

Extracts words from the text and normalizes them for analysis.

Words will be converted to lowercase so that different capitalization does not cause the same word to be counted as multiple unique words.

For example:

```text
Python python PYTHON
```

will be treated as the same word.

### `count_words(text)`

Returns the total number of extracted words.

### `count_sentences(text)`

Counts sentences using basic sentence-ending punctuation such as `.`, `!`, and `?`.

This will be a simple approximation rather than a full natural-language sentence detector.

### `count_paragraphs(text)`

Counts non-empty paragraphs separated by blank lines.

Multiple consecutive blank lines should not create additional paragraphs.

### `count_unique_words(text)`

Counts the number of distinct normalized words.

### `most_common_words(text, n=10)`

Uses Python's `Counter` to identify the most frequently occurring words.

The default will be the 10 most common words.

### `average_word_length(text)`

Calculates the average length of the extracted words.

If there are no words, the function should return `0` rather than causing a division-by-zero error.

### `readability_score(text)`

Calculates a basic readability score using the Flesch Reading Ease formula.

Because accurate syllable detection requires more sophisticated natural-language processing, the project will use a simple rule-based syllable approximation.

The README will document that the readability score is an estimate rather than an exact linguistic measurement.

### `analyze_text(text)`

Acts as a higher-level function that combines the individual analysis functions and returns the complete set of results.

This allows the command-line interface to request the analysis without knowing the details of how each metric is calculated.

---

## 5. Command-Line Interface Design

The application will be run from the command line using a command such as:

```text
python main.py sample.txt
```

The CLI will:

1. Receive the file path.
2. Check whether the file exists.
3. Read the file.
4. Pass the text to the analysis module.
5. Display the results in a readable report.

For an invalid file path, the program should display a clear error message rather than an unhandled Python traceback.

For example:

```text
Error: File 'missing.txt' was not found.
```

The CLI should remain simple and should not require a command-line framework.

---

## 6. Design Decisions and Potential Concerns

### Word Definition

Words will be extracted using a simple regular-expression-based approach rather than a natural-language processing library.

Punctuation should not be treated as part of a word.

Words will be normalized to lowercase for frequency and uniqueness calculations.

### Sentence Definition

A sentence will be identified using basic sentence-ending punctuation.

This approach is intentionally simple and may not correctly handle cases such as abbreviations.

For example:

```text
Dr. Smith went home.
```

could cause a basic sentence detector to produce an inaccurate result.

This limitation is acceptable for the scope of the project.

### Paragraph Definition

A paragraph will be considered a block of non-empty text separated from another block by blank lines.

### Readability

The readability score will be an approximation because syllable counting will use a simple rule-based method.

The project should not add a large NLP library simply to improve this one calculation.

### Empty Input

The application must handle empty text without crashing.

Metrics that depend on the number of words or sentences should return a sensible value such as `0`.

### File Encoding

The application will assume normal UTF-8 text files. Common file-reading errors should be handled with a clear user-facing message.

### Scope

The application is intended for basic English text analysis rather than full linguistic analysis.

---

## 7. Testing Strategy

Testing will use `pytest`.

The primary focus will be testing the analysis functions independently from the command-line interface.

### Typical Test Cases

Tests should cover:

- Character counting.
- Word counting.
- Sentence counting.
- Paragraph counting.
- Unique word counting.
- Most common words.
- Average word length.
- Readability calculation.
- A complete `analyze_text()` result.

### Normalization Tests

The analyzer should treat different capitalization of the same word as the same word.

Example:

```text
Data data DATA
```

should result in one unique word.

### Punctuation Tests

Test text containing punctuation such as:

```text
Hello, world! How are you?
```

to make sure punctuation does not incorrectly become part of the words.

### Paragraph Tests

Test multiple paragraphs separated by blank lines.

Also test multiple consecutive blank lines.

### Edge Cases

Tests should include:

1. Empty text.
2. Whitespace-only text.
3. A single word.
4. Repeated words.
5. Text with different capitalization.
6. Text containing punctuation.
7. Text with multiple paragraphs.
8. Text with no sentence-ending punctuation.
9. Readability calculation with empty input.

### CLI Tests

A small number of tests should verify:

- A valid file can be processed.
- A nonexistent file produces an appropriate error.

The project does not need extensive CLI testing because the main focus is the text-analysis logic.

---

## 8. Manual Verification Plan

After implementation, the application should be manually tested using `sample.txt`.

A sample file will contain multiple sentences, repeated words, and multiple paragraphs.

The application will be run with:

```text
python main.py sample.txt
```

The manual verification will confirm that:

- The program starts successfully.
- The file is read correctly.
- All requested metrics are displayed.
- The results are reasonable.
- The most common words are displayed.
- The readability score is displayed.
- The report is readable.

An invalid file will also be tested:

```text
python main.py missing.txt
```

The expected behavior is a clear error message rather than an unhandled traceback.

The final project will also be verified using:

```text
pytest
```

and:

```text
ruff check .
```

Both checks should pass before the project is considered complete.

---

## 9. README Documentation Plan

The README should contain the following sections:

### Project Overview

A short description of the Text Analyzer and its purpose.

### Features

A list of the supported text-analysis metrics.

### Project Structure

A brief explanation of the major files and their responsibilities.

### Requirements

The required Python version and development tools.

### Installation

Instructions for installing the required dependencies.

### Usage

An example showing how to run the application:

```text
python main.py sample.txt
```

along with an example of the resulting report.

### Testing

Instructions for running:

```text
pytest
```

### Code Quality

Instructions for running:

```text
ruff check .
```

### Design Decisions and Limitations

Documentation of the simple word, sentence, paragraph, and syllable-counting approaches.

### AI-Assisted Development

A description of how AI was used during the different stages of development, including architecture, implementation, testing, and review.

---

## 10. Scope Control

The project will intentionally remain small.

The following features are outside the scope of this project:

- GUI or web interface.
- Database.
- External API.
- External dataset.
- Machine learning.
- Sentiment analysis.
- Language detection.
- PDF or Word document processing.
- Charts or dashboards.
- Advanced NLP libraries.
- Multiple-file batch processing.
- Cloud deployment.

These features are not necessary to demonstrate the AI-assisted development workflow and would add unnecessary complexity.

---

## 11. Proposed Development Workflow

The project will be developed in separate stages.

### Stage 1 — Architect

Define:

- Project requirements.
- Project structure.
- Functions.
- Design decisions.
- Edge cases.
- Testing strategy.
- Manual verification plan.
- Documentation requirements.

**This document represents the Architect stage.**

### Stage 2 — Builder

Implement the architecture by:

- Creating the project structure.
- Implementing the analysis functions.
- Implementing the CLI.
- Adding the initial tests.
- Adding project configuration.

### Stage 3 — Tester

Run the automated tests and add or improve tests for discovered edge cases.

The project should be verified using pytest.

### Stage 4 — Reviewer / Refactoring

Review the implementation for:

- Readability.
- Maintainability.
- Duplicate code.
- Error handling.
- Function design.
- Documentation.
- Code quality.

Ruff will be used to identify and correct code-quality issues.

### Stage 5 — Final Verification

Confirm that:

- Tests pass.
- Ruff passes.
- The CLI works manually.
- The README is complete.
- The repository contains only necessary project files.
- The final implementation matches the original architecture.

---

## 12. Definition of Done

The project will be considered complete when:

- A user can provide a `.txt` file from the command line.
- The program produces all requested analysis metrics.
- Empty and common invalid inputs are handled appropriately.
- Automated tests cover normal and edge cases.
- All tests pass.
- Ruff reports no code-quality issues.
- The application has been manually verified.
- The README explains installation, usage, testing, design decisions, and limitations.
- The implementation remains within the planned small scope.
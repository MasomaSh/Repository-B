from text_analyzer.analyzer import (
    analyze_text,
    average_word_length,
    count_characters,
    count_paragraphs,
    count_sentences,
    count_unique_words,
    count_words,
    extract_words,
    most_common_words,
    readability_score,
)


def test_count_characters():
    assert count_characters("Hello") == 5


def test_count_words():
    assert count_words("Hello world") == 2


def test_count_sentences():
    text = "Hello world! How are you? I am fine."
    assert count_sentences(text) == 3


def test_count_paragraphs():
    text = "First paragraph.\n\nSecond paragraph."
    assert count_paragraphs(text) == 2


def test_multiple_blank_lines_do_not_create_paragraphs():
    text = "First paragraph.\n\n\nSecond paragraph."
    assert count_paragraphs(text) == 2


def test_count_unique_words():
    text = "Data data DATA science"
    assert count_unique_words(text) == 2


def test_punctuation_is_not_part_of_words():
    text = "Hello, world!"
    assert count_words(text) == 2


def test_most_common_words():
    text = "apple apple banana banana banana orange"
    assert most_common_words(text, 2) == [
        ("banana", 3),
        ("apple", 2),
    ]


def test_average_word_length():
    text = "cat dog"
    assert average_word_length(text) == 3


def test_average_word_length_empty_text():
    assert average_word_length("") == 0


def test_readability_empty_text():
    assert readability_score("") == 0


def test_empty_text():
    results = analyze_text("")

    assert results["characters"] == 0
    assert results["words"] == 0
    assert results["sentences"] == 0
    assert results["paragraphs"] == 0
    assert results["unique_words"] == 0
    assert results["most_common_words"] == []
    assert results["average_word_length"] == 0
    assert results["readability_score"] == 0


def test_analyze_text():
    text = "Hello world. Hello Python."

    results = analyze_text(text)

    assert results["characters"] == len(text)
    assert results["words"] == 4
    assert results["sentences"] == 2
    assert results["paragraphs"] == 1
    assert results["unique_words"] == 3
    assert results["most_common_words"][0] == ("hello", 2)


def test_whitespace_only_text():
    text = "   \n\n   "

    assert count_words(text) == 0
    assert count_sentences(text) == 0
    assert count_paragraphs(text) == 0
    assert count_unique_words(text) == 0


def test_punctuation_only_text():
    text = "!!! ??? ..."

    assert count_words(text) == 0
    assert count_unique_words(text) == 0
    assert average_word_length(text) == 0


def test_apostrophes_in_words():
    text = "Don't stop. It's working."

    assert "don't" in extract_words(text)
    assert "it's" in extract_words(text)


def test_word_count_is_case_insensitive():
    text = "Python python PYTHON"

    assert count_words(text) == 3
    assert count_unique_words(text) == 1
    assert most_common_words(text, 1) == [("python", 3)]


def test_multiple_sentence_punctuation():
    text = "Really?! Yes!"

    assert count_sentences(text) == 2
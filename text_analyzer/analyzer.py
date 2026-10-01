import re
from collections import Counter


def count_characters(text):
    """Return the number of characters in the text."""
    return len(text)


def extract_words(text):
    """Extract lowercase words from the text."""
    return re.findall(r"\b[\w']+\b", text.lower())


def count_words(text):
    """Return the total number of words."""
    return len(extract_words(text))


def count_sentences(text):
    """Return an approximate number of sentences."""
    sentences = re.findall(r"[.!?]+", text)
    return len(sentences)


def count_paragraphs(text):
    """Return the number of non-empty paragraphs."""
    paragraphs = re.split(r"\n\s*\n", text.strip())

    if not text.strip():
        return 0

    return len(paragraphs)


def count_unique_words(text):
    """Return the number of unique words."""
    return len(set(extract_words(text)))


def most_common_words(text, n=10):
    """Return the n most common words and their counts."""
    words = extract_words(text)
    return Counter(words).most_common(n)


def average_word_length(text):
    """Return the average word length."""
    words = extract_words(text)

    if not words:
        return 0

    total_length = sum(len(word) for word in words)
    return total_length / len(words)


def count_syllables(word):
    """Estimate the number of syllables in a word."""
    word = word.lower()
    word = re.sub(r"[^a-z]", "", word)

    if not word:
        return 0

    vowels = "aeiouy"
    syllables = 0
    previous_was_vowel = False

    for char in word:
        is_vowel = char in vowels

        if is_vowel and not previous_was_vowel:
            syllables += 1

        previous_was_vowel = is_vowel

    if word.endswith("e") and syllables > 1:
        syllables -= 1

    return max(1, syllables)


def readability_score(text):
    """Calculate an approximate Flesch Reading Ease score."""
    words = extract_words(text)
    sentences = count_sentences(text)

    if not words or sentences == 0:
        return 0

    total_syllables = sum(count_syllables(word) for word in words)

    score = (
        206.835
        - 1.015 * (len(words) / sentences)
        - 84.6 * (total_syllables / len(words))
    )

    return score


def analyze_text(text):
    """Return all text-analysis metrics."""
    return {
        "characters": count_characters(text),
        "words": count_words(text),
        "sentences": count_sentences(text),
        "paragraphs": count_paragraphs(text),
        "unique_words": count_unique_words(text),
        "most_common_words": most_common_words(text),
        "average_word_length": average_word_length(text),
        "readability_score": readability_score(text),
    }
import spacy
from collections import Counter


def perform_ngram_study(text, n):
    # Load the English language model in spaCy
    nlp = spacy.load("en_core_web_sm")

    # Preprocess the text
    doc = nlp(text.lower())
    tokenized_text = [
        token.text for token in doc if not token.is_punct and not token.is_space
    ]

    # Generate n-grams
    ngrams = [
        tuple(tokenized_text[i : i + n]) for i in range(len(tokenized_text) - n + 1)
    ]

    # Count the occurrences of n-grams
    ngram_counts = Counter(ngrams)

    # Sort the n-grams by frequency in descending order
    sorted_ngrams = sorted(ngram_counts.items(), key=lambda x: x[1], reverse=True)

    # Return the sorted n-grams
    return sorted_ngrams


# Example usage
with open("../../docs/cleaned/uber-tos-uk-base.txt") as f:
    text = f.read()

n = 3

result = perform_ngram_study(text, n)

for ngram, count in result:
    print(" ".join(ngram), "-", count)

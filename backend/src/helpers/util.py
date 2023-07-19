def clean_space(doc):
    cleaned_text = []
    for token in doc:
        if not token.is_space:
            cleaned_text.append(token.text)
    return " ".join(cleaned_text)


def clean_lower(doc):
    cleaned_text = []
    for token in doc:
        if not token.is_space:
            cleaned_text.append(token.text.lower())
    return " ".join(cleaned_text)


def clean_lemma(doc):
    cleaned_text = []
    for token in doc:
        if not token.is_space:
            cleaned_text.append(token.lemma_)
    return " ".join(cleaned_text)

from spacy.matcher import Matcher

obligation_verbs = [
    "must",
    "have to",
    "need to",
    "should",
    "ought to",
    "shall",
    "will",
    "would have to",
    "may",
    "are to",
]


def identify_user_obligations(nlp, doc):
    obligation_sentences = []

    # Define patterns for obligation matching
    obligation_patterns = [
        # 1
        [
            {"LOWER": "you", "DEP": "nsubj", "OP": "+"},
            {"LOWER": {"IN": obligation_verbs}, "DEP": "aux", "OP": "+"},
        ],
        # 2
        [
            {"POS": {"IN": ["NOUN", "PROPN"]}, "LEMMA": "user", "OP": "+"},
            {"LOWER": {"IN": obligation_verbs}, "DEP": "aux", "OP": "+"},
        ],
        # 3
        [
            {"LOWER": "you", "DEP": "nsubj", "OP": "+"},
            {"LOWER": {"IN": ["agree", "consent", "confirm"]}, "OP": "+"},
        ],
        [
            {"LOWER": "you", "DEP": "nsubj", "OP": "+"},
            {"LOWER": "are", "OP": "+"},
            {"LOWER": "liable", "OP": "+"},
        ],
        # 4
        [
            {"POS": {"IN": ["NOUN", "PROPN"]}, "LEMMA": "user", "OP": "+"},
            {"LEMMA": {"IN": ["agree", "consent", "confirm"]}, "OP": "+"},
        ],
        [
            {"POS": {"IN": ["NOUN", "PROPN"]}, "LEMMA": "user", "OP": "+"},
            {"POS": "AUX", "OP": "*"},
            {"LOWER": "liable", "OP": "+"},
        ],
        # 5
        [
            {"LOWER": "you", "DEP": "nsubj", "OP": "+"},
            {"LEMMA": "do", "POS": "AUX", "OP": "+"},
            {"LEMMA": "not", "DEP": "neg", "OP": "+"},
            {
                "LEMMA": {"IN": ["agree", "consent", "confirm"]},
                "POS": "VERB",
                "OP": "+",
            },
        ],
        [
            {"POS": {"IN": ["NOUN", "PROPN"]}, "LEMMA": "user", "OP": "+"},
            {"LEMMA": "do", "POS": "AUX", "OP": "+"},
            {"LEMMA": "not", "DEP": "neg", "OP": "+"},
            {
                "LEMMA": {"IN": ["agree", "consent", "confirm"]},
                "POS": "VERB",
                "OP": "+",
            },
        ],
    ]

    matcher = Matcher(nlp.vocab)
    matcher.add("obligation_patterns", obligation_patterns)
    matches = matcher(doc)

    for id, start, end in matches:
        obligation_sentence = doc[start:end].sent
        obligation_sentences.append(obligation_sentence.text)

    return list(set(obligation_sentences))

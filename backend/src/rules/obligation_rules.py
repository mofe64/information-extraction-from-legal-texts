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
        # v1 patterns
        [{"LOWER": "you", "DEP": "nsubj", "OP": "+"}, {"POS": "VERB", "OP": "+"}],
        [
            {"LOWER": "you", "DEP": "nsubj", "OP": "+"},
            {"POS": "VERB", "OP": "+"},
            {"POS": "ADV", "OP": "+"},
        ],
        [
            {"LOWER": "you", "DEP": "nsubj", "OP": "+"},
            {"POS": "ADV", "OP": "+"},
            {
                "POS": "VERB",
                "OP": "+",
            },  # limit to obligation verbs (not possible since obligations are not always couches using obligation verbs)
        ],
        # v2 patterns - derived from uber look through
        [
            {"LOWER": "you", "DEP": "nsubj", "OP": "+"},
            {"LOWER": {"IN": obligation_verbs}, "DEP": "aux", "OP": "+"},
            {"POS": "VERB", "OP": "+"},
        ],
        # Noun phrase patterns eg "Users are responsible for maintaining the security of their login credentials."
        [
            {"POS": {"IN": ["NOUN", "PROPN"]}, "OP": "+"},
            {"POS": {"IN": ["ADJ", "PART"]}, "OP": "*"},
            {"LOWER": {"IN": obligation_verbs}, "DEP": "aux", "OP": "+"},
        ],
    ]

    matcher = Matcher(nlp.vocab)
    matcher.add("obligation_patterns", obligation_patterns)
    matches = matcher(doc)

    for id, start, end in matches:
        obligation_sentence = doc[start:end].sent
        obligation_sentences.append(obligation_sentence)

    return list(set(obligation_sentences))

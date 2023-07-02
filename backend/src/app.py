import spacy
from spacy.matcher import Matcher

nlp = spacy.load("en_core_web_sm")


with open("../docs/cleaned/uber-tos-uk-base.txt") as f:
    text = f.read()


def identify_user_obligations(doc):
    obligation_sentences = []

    # Define patterns for obligation matching
    obligation_patterns = [
        [{"LOWER": "you", "DEP": "nsubj", "OP": "+"}, {"POS": "VERB", "OP": "+"}],
        [
            {"LOWER": "you", "DEP": "nsubj", "OP": "+"},
            {"POS": "VERB", "OP": "+"},
            {"POS": "ADV", "OP": "+"},
        ],
        [
            {"LOWER": "you", "DEP": "nsubj", "OP": "+"},
            {"POS": "ADV", "OP": "+"},
            {"POS": "VERB", "OP": "+"},  # limit to obligation verbs
        ],
    ]

    matcher = Matcher(nlp.vocab)
    matcher.add("obligation_patterns", obligation_patterns)
    matches = matcher(doc)

    for id, start, end in matches:
        obligation_sentence = doc[start:end].sent
        obligation_sentences.append(obligation_sentence)

    return list(set(obligation_sentences))


def identify_privacy_related_sections(text):
    doc = nlp(text)
    matcher = Matcher(nlp.vocab)
    p1 = [
        {"LOWER": {"IN": ["personal", "personally identifiable"]}, "OP": "+"},
        {"LOWER": {"IN": ["data", "information"]}, "OP": "+"},
    ]
    p2 = [
        {"LEMMA": {"IN": ["collect", "process", "store"]}, "OP": "+"},
        {"LOWER": {"IN": ["data", "information"]}, "OP": "+"},
    ]
    p3 = [{"LOWER": {"IN": ["confidential", "private", "sensitive"]}, "OP": "+"}]
    p4 = [{"LOWER": {"IN": ["gdpr", "data protection"]}, "OP": "+"}]
    p5 = [
        {"LOWER": "share", "OP": "+"},
        {"LOWER": "data", "OP": "+"},
        {"LOWER": "with", "OP": "+"},
        {"LOWER": "third", "OP": "*"},
        {"ORTH": "-", "OP": "*"},
        {"LOWER": {"IN": ["party", "parties"]}, "OP": "*"},
        {"LOWER": {"IN": ["service", "services"]}, "OP": "*"},
        {"LOWER": {"IN": ["provider", "providers"]}, "OP": "*"},
    ]
    p6 = [{"LOWER": {"IN": ["gdpr", "data protection"]}, "OP": "+"}]

    matcher.add("PRIVACY_RULES", [p1, p2, p3, p4, p5, p6])

    matches = matcher(doc)

    privacy_sections = []
    for match_id, start, end in matches:
        section = doc[start:end].sent.text.strip()
        privacy_sections.append(section)

    return privacy_sections


doc = nlp(text)
x = identify_user_obligations(doc)
for i, sent in enumerate(x, 1):
    print(f" sentence {i}")
    print(sent)
    print()


# privacy_sections = identify_privacy_related_sections(text)
# for i, section in enumerate(privacy_sections, 1):
#     print(f"Privacy Section {i}:")
#     print(section)
#     print()

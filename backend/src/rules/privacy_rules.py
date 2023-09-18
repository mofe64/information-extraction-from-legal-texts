from spacy.matcher import Matcher

"""
Rule 1:
Pattern: Noun phrases containing "personal data" or "personally identifiable information" (PII)
Rationale: The phrases "personal data" and "personally identifiable information" explicitly refer to data that can be used to identify an individual.
Identifying such phrases can help pinpoint content related to privacy or data protection.

Rule 2:
Pattern: Verbs related to data collection or processing (e.g., "collect," "process," "store")
Rationale: Verbs associated with data collection or processing activities often indicate that user data is being handled.
Identifying these verbs can help identify sections where privacy-related activities are described.

Rule 3: Not applicable ...
Pattern: Adjectives describing sensitive information (e.g., "confidential," "private," "sensitive")
Rationale: Adjectives that qualify information as sensitive or confidential may indicate content related to privacy.
These descriptors suggest that the information being discussed requires special protection.

Rule 4:
Pattern: References to legal or regulatory frameworks (e.g., "GDPR," "CCPA," "data protection laws")
Rationale: Mentions of specific privacy laws or regulations suggest that the content relates to privacy or data protection.
Recognizing such references can help identify sections discussing compliance or legal aspects of privacy.

Rule 5:
Pattern: Phrases indicating data sharing or third-party involvement (e.g., "share data with," "third-party service provider")
Rationale: Phrases that refer to sharing data with external entities or involving third-party service providers often imply potential privacy implications. 
Identifying such phrases can help locate sections discussing data sharing practices.

Rule 6:
Pattern: Phrases indicating security measures (e.g., "encryption," "firewalls," "access controls")
Rationale: Mentions of security measures often signify a focus on protecting user data. 
Identifying these phrases can help identify sections discussing data security practices and privacy safeguards.
"""


def identify_privacy_related_sections(nlp, doc):
    privacy_sections = []
    privacy_patterns = [
        # Your personal data
        # Your personal information
        [
            {"LOWER": "your", "POS": "pron", "OP": "+"},
            {
                "POS": "ADJ",
                "DEP": "amod",
                "OP": "*",
            },
            {"LOWER": {"IN": ["data", "information"]}, "POS": "noun", "OP": "+"},
        ],
        # personal data on its own
        [
            {
                "LOWER": {
                    "IN": ["personal", "personally", "non-personally", "profile"]
                },
                "OP": "+",
            },
            {"LOWER": "identifiable", "OP": "*"},
            {"LOWER": {"IN": ["data", "information"]}, "OP": "+"},
        ],
        # uber used the information/data we collect ..
        # The data/information we collect is to ...
        [
            {
                "LOWER": {"IN": ["data", "information"]},
                "POS": "NOUN",
                "DEP": {"IN": ["dobj", "nsubj"]},
                "OP": "+",
            },
            {"POS": "PRON", "DEP": "nsubj", "OP": "*"},
            {
                "LEMMA": {"IN": ["collect", "process", "store", "access", "use"]},
                "OP": "*",
            },
        ],
        # collect/process/store/access/use adj data
        [
            {
                "LEMMA": {
                    "IN": ["collect", "process", "store", "access", "use", "disclose"]
                },
                "OP": "+",
            },
            {"POS": "ADJ", "DEP": "amod", "OP": "*"},
            {"LOWER": {"IN": ["data", "information"]}, "OP": "+"},
        ],
        # share user data
        [
            {"LOWER": "share", "POS": "VERB", "OP": "+"},
            {"LEMMA": "user", "OP": "+"},
            {"LOWER": "data", "OP": "+"},
        ],
        # share data with
        [
            {"LOWER": "share", "OP": "+"},
            {"LOWER": "data", "OP": "+"},
            {"LOWER": "with", "OP": "+"},
        ],
        # gdpr and other regs
        [
            {"LOWER": {"IN": ["gdpr"]}, "OP": "+"},
        ],
        [
            {"LOWER": {"IN": ["general"]}, "OP": "+"},
            {"LOWER": {"IN": ["data"]}, "OP": "+"},
            {"LOWER": {"IN": ["protection"]}, "OP": "+"},
            {"LOWER": {"IN": ["regulation"]}, "OP": "+"},
        ],
        [
            {"LOWER": {"IN": ["data"]}, "OP": "+"},
            {"LOWER": {"IN": ["protection"]}, "OP": "+"},
            {"LOWER": {"IN": ["act"]}, "OP": "+"},
        ],
        [
            {"LOWER": {"IN": ["privacy"]}, "OP": "+"},
            {"LOWER": {"IN": ["and"]}, "OP": "+"},
            {"LOWER": {"IN": ["communications"]}, "OP": "+"},
            {"LOWER": {"IN": ["regulation"]}, "OP": "+"},
        ],
        # encryption and other like terms
        [{"LEMMA": {"IN": ["encrypt", "encryption", "firewall"]}}],
    ]

    matcher = Matcher(nlp.vocab)
    matcher.add("PRIVACY_RULES", privacy_patterns)
    matches = matcher(doc)

    for id, start, end in matches:
        section = doc[start:end].sent
        privacy_sections.append(section.text)

    return list(set(privacy_sections))

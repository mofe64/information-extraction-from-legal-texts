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

Rule 3:
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
Pattern: Terms related to consent or user rights (e.g., "opt-in," "consent," "access rights," "data subject rights")
Rationale: Terms associated with consent or user rights highlight sections where privacy-related permissions or user protections are addressed. 
Recognizing these terms can help identify content discussing privacy choices or user control.

Rule 7:
Pattern: Phrases indicating security measures (e.g., "encryption," "firewalls," "access controls")
Rationale: Mentions of security measures often signify a focus on protecting user data. 
Identifying these phrases can help identify sections discussing data security practices and privacy safeguards.
"""

privacy_dictionary = {
    "personal information": [
        "PII",
        "personally identifiable information",
        "sensitive data",
    ],
    "data protection": ["information security", "privacy protection"],
    "consent": ["approval", "permission", "authorization"],
    "user privacy": ["individual privacy", "customer privacy"],
    "data breach": ["security incident", "information leak"],
    "anonymized data": ["de-identified data", "pseudonymized data"],
    "cookie": ["web cookie", "tracking cookie"],
    "opt-out": ["unsubscribe", "do not track"],
    "privacy policy": ["data protection policy", "information usage policy"],
    "GDPR": ["General Data Protection Regulation"],
    "data controller": ["data custodian", "data owner"],
    "data processor": ["service provider", "data handler"],
    "data subject": ["individual", "customer"],
    "data retention": ["data storage", "information preservation"],
    "third party": ["external party", "outside organization"],
    "data minimization": ["minimum necessary principle", "limited data collection"],
    "encryption": ["data encryption", "data security"],
    "tracking": ["monitoring", "surveillance"],
    "data erasure": ["data deletion", "right to be forgotten"],
    "data transfer": ["data sharing", "data transmission"],
}


def identify_privacy_related_sections(nlp, doc):
    privacy_sections = []
    privacy_patterns = [
        [
            {"LOWER": {"IN": ["personal", "personally identifiable"]}, "OP": "+"},
            {"LOWER": {"IN": ["data", "information"]}, "OP": "+"},
        ],
        [
            {"LEMMA": {"IN": ["collect", "process", "store"]}, "OP": "+"},
            {"LOWER": {"IN": ["data", "information"]}, "OP": "+"},
        ][{"LOWER": {"IN": ["confidential", "private", "sensitive"]}, "OP": "+"}],
        [{"LOWER": {"IN": ["gdpr", "data protection"]}, "OP": "+"}],
        [
            {"LOWER": "share", "OP": "+"},
            {"LOWER": "data", "OP": "+"},
            {"LOWER": "with", "OP": "+"},
            {"LOWER": "third", "OP": "*"},
            {"ORTH": "-", "OP": "*"},
            {"LOWER": {"IN": ["party", "parties"]}, "OP": "*"},
            {"LOWER": {"IN": ["service", "services"]}, "OP": "*"},
            {"LOWER": {"IN": ["provider", "providers"]}, "OP": "*"},
        ],
        [{"LOWER": {"IN": ["gdpr", "data protection"]}, "OP": "+"}],
    ]

    matcher = Matcher(nlp.vocab)
    matcher.add("PRIVACY_RULES", privacy_patterns)
    matches = matcher(doc)

    for id, start, end in matches:
        section = doc[start:end].sent
        privacy_sections.append(section)

    return list(set(privacy_sections))

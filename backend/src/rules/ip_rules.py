from spacy.matcher import Matcher


def identify_ip_related_sections(nlp, doc):
    ip_sections = []
    ip_patterns = [
        # infringes/violate copyright/trademark
        [
            {
                "LEMMA": {"IN": ["infringe", "violate"]},
                "POS": "VERB",
                "OP": "+",
            },
            {
                "LOWER": {"IN": ["copyright", "trademark"]},
                "POS": "NOUN",
                "OP": "+",
            },
        ],
        # copyrighted content/ works
        [
            {
                "LEMMA": "copyright",
                "OP": "+",
            },
            {
                "LEMMA": {"IN": ["content", "work"]},
                "POS": "NOUN",
                "OP": "+",
            },
        ],
        # copy right infringment
        [
            {"LOWER": "copyright", "OP": "+"},
            {"LOWER": "infringement", "OP": "+"},
        ],
        # fair use/dealing
        [
            {"LOWER": "fair", "OP": "+"},
            {"LOWER": {"IN": ["use", "dealing"]}, "OP": "+"},
        ],
        # person's/user's/another's copyright/trademark,
        [
            {
                "LEMMA": {"IN": ["user", "person", "another"]},
                "POS": "NOUN",
                "OP": "+",
            },
            {"POS": "PART", "DEP": "case", "OP": "*"},
            {"LOWER": {"IN": ["copyright", "content", "trademark"]}, "OP": "+"},
        ],
        # copyright/trademark violations/infringement
        [
            {"LOWER": {"IN": ["copyright", "trademark"]}, "OP": "+"},
            {"LEMMA": {"IN": ["violations", "infringment"]}, "OP": "+"},
        ],
        #  United States Digital Millennium Copyright Act
        [
            {"LOWER": "united", "OP": "+"},
            {"LOWER": "states", "OP": "+"},
            {"LOWER": "digital", "OP": "+"},
            {"LOWER": "millennium", "OP": "+"},
            {"LOWER": "copyright", "OP": "+"},
            {"LOWER": "act", "OP": "+"},
        ],
        # EU copyright directive / copyright directive
        [
            {"LOWER": "eu", "OP": "*"},
            {"LOWER": "copyright", "OP": "+"},
            {"LOWER": "directive", "OP": "+"},
        ],
        # Europeam union copyright directive
        [
            {"LOWER": "european", "OP": "+"},
            {"LOWER": "union", "OP": "+"},
            {"LOWER": "copyright", "OP": "+"},
            {"LOWER": "directive", "OP": "+"},
        ],
        # trademark rights
        [
            {"LOWER": "trademark", "OP": "+"},
            {"LOWER": "rights", "OP": "+"},
        ],
    ]
    matcher = Matcher(nlp.vocab)
    matcher.add("IP_RULES", ip_patterns)
    matches = matcher(doc)

    for id, start, end in matches:
        section = doc[start:end].sent
        ip_sections.append(section.text)

    return list(set(ip_sections))

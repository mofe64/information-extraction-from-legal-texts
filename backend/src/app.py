import spacy
from rules.obligation_rules import identify_user_obligations
from rules.privacy_rules import identify_privacy_related_sections
from rules.ip_rules import identify_ip_related_sections
from helpers.util import clean_lower, clean_space

nlp = spacy.load("en_core_web_sm")


with open("../docs/cleaned/uber-privacy-uk-base.txt") as f:
    text = f.read()

text = clean_space(nlp(text))
text = clean_lower(nlp(text))
# print(text[0:2000])
doc = nlp(text)
x = identify_user_obligations(nlp, doc)


# for i, sent in enumerate(x, 1):
#     print(f" sentence {i}")
#     print(sent)
#     print()


privacy_sections = identify_privacy_related_sections(nlp, doc)
for i, section in enumerate(privacy_sections, 1):
    print(f"Privacy Section {i}:")
    print(section)
    print()


# ip_sections = identify_ip_related_sections(nlp, doc)
# for i, section in enumerate(ip_sections, 1):
#     print(f"IP Section {i}:")
#     print(section)
#     print()

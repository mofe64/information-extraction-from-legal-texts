import spacy
from spacy.matcher import Matcher
from rules.obligation_rules import identify_user_obligations
from rules.privacy_rules import identify_privacy_related_sections

nlp = spacy.load("en_core_web_sm")


with open("../docs/cleaned/uber-tos-uk-base.txt") as f:
    text = f.read()


doc = nlp(text)
x = identify_user_obligations(nlp, doc)


for i, sent in enumerate(x, 1):
    print(f" sentence {i}")
    print(sent)
    print()


# privacy_sections = identify_privacy_related_sections(text)
# for i, section in enumerate(privacy_sections, 1):
#     print(f"Privacy Section {i}:")
#     print(section)
#     print()

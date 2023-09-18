import spacy

nlp = spacy.load("en_core_web_sm")


test = [
    nlp(word.lower())[0]
    for word in [
        "royalty-free",
        "sublicencable",
        "non-transferable",
        "non-exclusive",
    ]
]
test2 = [c.lemma_ for c in test]
print(test)
print(test2)


def get_pos(text):
    pos_arr = []
    doc = nlp(text)
    for token in doc:
        if token.is_punct:
            pos_arr.append(" ")
        elif token.is_space:
            pos_arr.append(" ")
        else:
            pos_arr.append(token.pos_)

    return " ".join(pos_arr)


def get_dep(text):
    pos_arr = []
    doc = nlp(text)
    for token in doc:
        if token.is_punct:
            pos_arr.append(" ")
        elif token.is_space:
            pos_arr.append(" ")
        else:
            pos_arr.append(token.dep_)

    return " ".join(pos_arr)


z = "We retain the data we collect for different periods of time depending on what it is, how we use it, and how you configure your settings"
print("pos -> " + get_pos(z))
print("dep -> " + get_dep(z))
print(spacy.explain("dobj"))

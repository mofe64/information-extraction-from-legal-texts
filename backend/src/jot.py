import spacy

nlp = spacy.load("en_core_web_sm")


test = [nlp(word.lower())[0] for word in ["encrypt", "person's"]]
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


z = "The licence to your content that you grant to us"
print("pos -> " + get_pos(z))
print("dep -> " + get_dep(z))
print(spacy.explain("dobj"))

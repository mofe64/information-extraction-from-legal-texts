import spacy

nlp = spacy.load("en_core_web_sm")


test = [nlp(word.lower())[0] for word in ["collecting", "processed", "stored"]]
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


z = "You must read carefully and agree to the Terms prior to accessing and using Uber’s App(s)/Website(s) Services or Uber Products. These Terms expressly supersede prior agreements or arrangements about the App(s)/Websites Services (as defined below) and Uber Products between you and Uber."

# print(get_pos(z))
# print(get_dep(z))
print(spacy.explain("neg"))

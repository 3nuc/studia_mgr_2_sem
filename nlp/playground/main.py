import spacy


text = open('./przyklad.txt').read()
nlp = spacy.load('en_core_web_sm')

doc = nlp(text)
tokens = doc


def filterBadStuff(token):
    return token.pos_ not in ['PUNCT', 'SYM', 'NUM', 'SPACE']


tokens = filter(filterBadStuff, tokens)

# drop dupes
tokens = list(dict.fromkeys(tokens))

for token in tokens:
    print(token.text, token.pos_)

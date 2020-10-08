import spacy
import random
import string


text = open('./przyklad.txt').read()
nlp = spacy.load('en_core_web_sm')

doc = nlp(text)
tokens = doc


def filterBadStuff(token):
    return token.pos_ not in ['PUNCT', 'SYM', 'NUM', 'SPACE']


tokens = filter(filterBadStuff, tokens)

# drop dupes
tokens = list(dict.fromkeys(tokens))


# for token in tokens:
#     print(token.text, token.pos_)


class ScrambleOperations:
    @staticmethod
    def swap_letter(text):
        copy = text
        letter_index_to_swap = random.randrange(0, len(copy)-1)
        as_list = list(copy)
        as_list[letter_index_to_swap] = random.choice(string.ascii_letters)
        return "".join(as_list)


print(ScrambleOperations.swap_letter('fofofofofo'))

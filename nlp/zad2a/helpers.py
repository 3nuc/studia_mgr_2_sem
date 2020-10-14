
# Filters out non-word token positions
import random
import string
import spacy
import Levenshtein

def is_word_token(token):
    return token.pos_ not in ['PUNCT', 'SYM', 'NUM', 'SPACE']

def get_random_letter():
    return random.choice(string.ascii_letters)

class ScrambleOperations:
    @staticmethod
    def swap_letter(text):
        letter_index_to_swap = 0 if len(text) == 1 else random.randrange(0, len(text)-1)
        as_list = list(text)
        as_list[letter_index_to_swap] = get_random_letter()
        return "".join(as_list)

    @staticmethod
    def remove_letter(text):
        letter_index_to_remove = 0 if len(text) == 1 else random.randrange(0, len(text)-1)
        as_list = list(text)
        as_list.remove(as_list[letter_index_to_remove])
        return "".join(as_list)

    @staticmethod
    def add_letter(text):
        as_list = list(text)
        as_list.append(get_random_letter())
        return "".join(as_list)
    
def get_tokens():
    nlp = spacy.load('en_core_web_sm')
    f_read = open('./przyklad.txt', 'r')
    text = f_read.read()
    f_read.close()
    return filter(is_word_token, nlp(text))

def write_tokens(tokens):
    f_write = open('./przyklad_scrambled.txt', 'w');
    f_write.write('\n'.join(tokens));
    f_write.close();
    
def get_best_distance_match(scrambled_text, original_text_array):
    min = 2**64-1
    closest_match = original_text_array[0]
    for original in original_text_array:
        distance = Levenshtein.distance(original, scrambled_text)
        if (distance < min):
           closest_match = original
           min = distance
    
    return closest_match

def get_number_of_mistakes(array1, array2):
    count = 0;
    for i in range(len(array1)):
        if (array1[i] != array2[i]):
            count = count + 1;
    return count


import random
import math
import helpers
import spacy


original_tokens = helpers.get_tokens()
original_tokens = map(lambda token: token.text,original_tokens)
original_tokens = list(dict.fromkeys(original_tokens))

tokens = helpers.get_tokens()
tokens = map(lambda token: token.text,tokens)
# drop dupes
tokens = list(dict.fromkeys(tokens))

tokens_count = len(tokens)
twenty_percent = math.ceil(tokens_count*0.2)

token_indices_to_scramble = random.sample(
    range(1, tokens_count), twenty_percent)

for index in token_indices_to_scramble:
    operations = [helpers.ScrambleOperations.add_letter,
                  helpers.ScrambleOperations.remove_letter, helpers.ScrambleOperations.swap_letter]
    tokens[index] = random.choice(operations)(tokens[index])

helpers.write_tokens(tokens)

for index in range(len(tokens)):
    tokens[index] = helpers.get_best_distance_match(tokens[index], original_tokens);
    print(tokens[index], original_tokens[index], '\n')

mistake_count = helpers.get_number_of_mistakes(tokens, original_tokens)
print("Number of mistakes that weren't fixed:", mistake_count, "out of", len(tokens))
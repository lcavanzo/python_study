#!python3

'''
text_replacement.py -  reads in text files and lets the user add their
   own text anywhere the word ADJECTIVE, NOUN, ADVERB, or VERB
   appears in the text file.
'''
import re

with open("text_file.txt", 'r') as file:

    regex_adj = r'ADJECTIVE'
    regex_noun = r'NOUN'
    regex_adv = r'ADVERB'
    regex_verb = r'VERB'

    new_text = []
    for line in file:
        for word in line.split():
            if re.match(regex_adj, word):
                ans = input(f'Enter an {word.lower()}: ')
                word = ans
            elif re.match(regex_noun, word):
                ans = input(f'Enter a {word.lower()}: ')
                word = ans
            elif re.match(regex_adv, word):
                ans = input(f'Enter a {word.lower()}: ')
                word = ans
            elif re.match(regex_verb, word):
                ans = input(f'Enter a {word.lower()}: ')
                word = ans
            new_text.append(word)
        new_text.append('\n')

message = ' '.join(new_text)
print(message)

with open('return_text_file.txt', 'w') as file:
    file.write(message)

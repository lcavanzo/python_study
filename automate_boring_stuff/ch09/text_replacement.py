#! python3
'''
text_replacement.py -  reads in text files and lets the user add their
   own text anywhere the word ADJECTIVE, NOUN, ADVERB, or VERB
   appears in the text file.
'''
import re

#TODO: Read text file
with open("text_file.txt", 'r') as file:

#TODO: Look for ADJECTIVE,NOUN,ADVERB or VERB in the file provided
#TEST: create regex for matching the words then replace them in a for loop ???
    WORDS = ['ADJECTIVE','NOUN','ADVERB','VERB']
    print(WORDS)
    for line in file:
        for word in line.split():
            if word in WORDS:
                ans = input(f'Enter a {word.upper()}: ')

        print(line)

#TODO: Ask words for replace the ADV, NOUN, ADVER or VERB
#TODO: Print new sentences
#TODO: Save sentences to a file


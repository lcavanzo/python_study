#!python3

'''
text_replacement.py -  reads in text files and lets the user add their
   own text anywhere the word ADJECTIVE, NOUN, ADVERB, or VERB
   appears in the text file.
'''
import re

# Getting content of the file
with open("text_file.txt", 'r', encoding="utf-8") as file:
    content = file.read()

W_REGEX = re.compile(r'\bADJECTIVE\b|\bNOUN\b|\bVERB\b|\bADVERB\b')

while True:
    match = W_REGEX.search(content)
    ans = ''
    if match is None:
        break
    elif match.group() == "ADJECTIVE" or  match.group() == "ADVERB":
        ans = input(f"Enter an {match.group()}: ")
    elif match.group() == "NOUN" or  match.group() == "VERB":
        ans = input(f"Enter a {match.group()}: ")
    content = re.sub(W_REGEX,ans, content, 1)
print(content)

with open('return_text_file.txt', 'w', encoding='utf-8') as file:
    file.write(content)

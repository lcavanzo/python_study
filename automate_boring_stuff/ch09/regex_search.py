#!python 3


'''
regex_search.py - A program that opens all .txt files in a folder and searches for any line
that matches a user-supplied regular expression. The results should be printed to the screen.
'''

import re
from pathlib import Path

# Asking to the user what to search for.
user_input = input("Enter a word to search for searhing: ")
escaped_input = re.escape(user_input)  # Escape special characters

USER_REGEX = re.compile(rf"\b{escaped_input}\b")

# searching the word that the user is looking for
cwd = Path.cwd().glob('*.txt')
flag = False
for f in cwd:
    if f.is_file():
        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()
            match = USER_REGEX.search(content)
            if match:
                print(f'file: {file.name} Pattern Found: {match.group()}')
                flag = True
    else:
        continue
if flag == False:
    print("No Matches Found")

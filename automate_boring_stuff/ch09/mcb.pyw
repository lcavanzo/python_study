#! python3
# mcb.pyw - Saves and loads pieces of text ot the clipboard.
'''
Usage python mcb.pyw save <keyword> - Saves clipboard to keyword.
    python mcb.pyw <keyword> - Loads keyword to clipboard.
    python mcb.pyw list - Loads all keywords to clipboard.
    python mcb.pyw delete <keyword> - Delete a keyword from the shelf
    python mcb.pyw delete - Delete all keyword in the shelf
'''

import shelve
import sys

import pyperclip

mcb_shelf = shelve.open('mcb')

# Save clipboard content.
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcb_shelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
    del mcb_shelf[sys.argv[2]]
elif len(sys.argv) == 2:
    # list keywords and laod content.
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcb_shelf.keys())))
    if sys.argv[1].lower() == 'delete':
        mcb_shelf.clear()
    elif sys.argv[1] in mcb_shelf:
        pyperclip.copy(mcb_shelf[sys.argv[1]])

mcb_shelf.close()

"""Load a text file as a list

Arguments:
    - text file name (and directy path if needed

Exceptions:
    - IOError if file name not found

Returns:
    - A list of all words in a text file in lower case

Requires import sys
"""

import sys

def load(file):
    """Open a text file and return a list of lowercase strings"""
    try:
        with open(file) as in_file:
            loaded_txt = in_file.read().strip().split('\n')
            loaded_txt = [x.lower() for x in loaded_txt]
            return loaded_txt
    except IOError as e:
        print(f"{e}\n Error opening {file}")
        sys.exit(1)

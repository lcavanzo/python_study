"""
Your goal is to build a function count_words(text) that takes a string of text and returns a dictionary where keys a
re words and values are their counts.
The function should treat words as case-insensitive and ignore punctuation.
"""

from typing import Dict


def count_words(text: str) -> Dict:
    if text == "":
        return {}
    words = text.lower().split()
    countWords = {}
    for word in words:
        word = word.strip("!.,")
        if word not in countWords:
            countWords[word] = 1
        else:
            countWords[word] += 1
    return countWords


"""
def count_words(text: str) -> Dict[str, int]: # See next point for Dict[str, int]
    if not text: # More Pythonic check for empty string
        return {}

    # Create a translation table to replace punctuation with spaces
    # This ensures that "word1-word2" becomes "word1 word2" and splits correctly
    translator = str.maketrans(string.punctuation, ' ' * len(string.punctuation))
    clean_text = text.lower().translate(translator)

    # Split by whitespace, and filter out any empty strings that might result
    # from multiple spaces or punctuation at the start/end
    words = [word for word in clean_text.split() if word]

    # Use collections.Counter for a more Pythonic and efficient count (see point 3)
    from collections import Counter
    return dict(Counter(words))
"""

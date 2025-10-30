"""
Task: Create another new Python file (e.g., string_utils.py) and define a function is_palindrome(text) that returns True if the input text is a palindrome (reads the same forwards and backward), and False otherwise.

It should ignore case and non-alphanumeric characters (e.g., "A man, a plan, a canal: Panama" is a palindrome).
'a man a plan a canal Panama'
'amanap lanac a nalp a nam a'

Hint: You might need to preprocess the string (convert to lowercase, remove non-alphanumeric characters) before checking.
The str.lower(), str.isalnum() methods, and string slicing ([::-1]) might be useful.
"""

import string


def is_palindrome(text: str) -> bool:
    """Validate if a text is a palindrome"""
    if isinstance(text, str):
        translator = str.maketrans(string.punctuation, " " * len(string.punctuation))
        clean_text = text.lower().translate(translator).replace(" ", "")
        # This regex matches any character that is NOT a lowercase letter (a-z) or a digit (0-9).
        # clean_text = re.sub(r'[^a-z0-9]', '', text.lower())
        if clean_text == clean_text[::-1]:
            # print("True")
            return True
        else:
            # print("False")
            return False
    raise TypeError("Input for is_palindrome must be a string.")


if __name__ == "__main__":
    is_palindrome("A man, a plan, a canal: Panama")
    is_palindrome("Luis")

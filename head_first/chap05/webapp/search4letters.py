
def search4letters(phrase:str, letters:str='aeiou') -> set:
    """Return a set of letters found in a supplied phrase"""
    return set(letters).intersection(set(phrase))


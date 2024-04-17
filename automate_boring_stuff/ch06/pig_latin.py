# Pig_latin.

"""
Pig Latin is a silly made-up language that alters English words.
If a word begins with a vowel, the word yay is added to the end of it.
If a word begins with a consonant or consonant cluster (like ch or gr),
that consonant or cluster is moved to the end of the word followed by ay.
"""
# English to Pig Latin
print("Enter the English message to translate into Pig Latin: ")
message = input()

VOWELS = ("a", "e", "i", "o", "u", "y")

pig_latin = []  # A lsit of the words in Pig Latin
for word in message.split():
    # Separate the non-letters at the start of this word
    prefix_non_letters = ""
    while len(word) > 0 and not word[0].isalpha():
        prefix_non_letters += word[0]
        word = word[1:]
    if len(word) == 0:
        pig_latin.append(prefix_non_letters)
        continue

    # Separate the non-letters at the end of this word:
    suffix_non_letters = ""
    while not word[-1].isalpha():
        suffix_non_letters += word[-1] + suffix_non_letters
        word = word[:-1]

    # Remember if the word was in uppercase or title case.
    was_upper = word.isupper()
    was_title = word.istitle()

    word = word.lower()  # Make the word lowercase for translation

    # Separete the consonants at the start of this word:
    prefix_consonants = ""
    while len(word) > 0 and not word[0] in VOWELS:
        prefix_consonants += word[0]
        word = word[1:]

    # Add the Pig Latin ending to the word
    if prefix_consonants != "":
        word += prefix_consonants + "ay"
    else:
        word += "yay"

    # Set the word back to uppercase or title case:
    if was_upper:
        word = word.upper()
    if was_title:
        word = word.title()

    # Add the non-letters back to the start or end of the word
    pig_latin.append(prefix_non_letters + word + suffix_non_letters)

# Join all the words back together into a single string
print(" ".join(pig_latin))

"""
    Convert english words to a pig latin
    To form Pig Latin, you take an English word that begins with a
    consonant, move that consonant to the end, and then add “ay” to the
    end of the word. If the word begins with vowel, you simply add “way”
    to the end of the word.
"""

consonants = ('b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n',
                'p', 'q', 'r', 's', 't', 'v', 'w', 'x' , 'y', 'z'
)
vowels = ('a', 'e', 'i', 'o', 'u')

def consonants_2_pig_latin(my_word):
    """Convert to a pig latin if 'word' starts with a consonant"""
    while True:
        first_letter = my_word[:1]
        if first_letter in vowels:
            my_word =f"{word}ay"
            return my_word
            break
        else:
            my_word =f"{word[1:]}{first_letter}"

def vowels_2_pig_latin(my_word):
    """Convert to a pig latin if 'word' starts with a vowel"""
    my_word =f"{word}yay"
    return my_word

while True:
    word = input("Word to convert to a Pig latin: ")

    if word[:1] in vowels:
        new_word = vowels_2_pig_latin(word)
    else:
        new_word = consonants_2_pig_latin(word)

    print(new_word)

    answer = input("Other word('y' to continue): ")
    if answer.lower() != 'y':
        print("bye")
        break

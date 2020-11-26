import load_dictionary

FILENAME = 'random_words.txt'
word_list = load_dictionary.load(FILENAME)

anagram_list = []

user_input = input("Input name = ")
user_input = user_input.lower()

# Sort name and find anagrams
user_input_sorted = sorted(user_input)
for word in word_list:
    word = word.lower()
    if word != user_input:
        if sorted(word) == user_input_sorted:
            anagram_list.append(word)
# print out list of anagrams
if len(anagram_list) == 0:
    print("You need a larger dictionary or a new name")
else:
    print("Anagrams = ", sep='')
    print(*anagram_list, sep='\n')


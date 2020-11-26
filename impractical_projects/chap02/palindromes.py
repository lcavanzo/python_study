"""Find palindromes (letter palingrams) in a dictionary file"""
import load_dictionary

FILENAME = "multiple_words.txt"
word_list = load_dictionary.load(FILENAME)
pali_list = []

for word in word_list:
    if len(word) > 1 and word == word[::-1]:
        pali_list.append(word)

print(f"number of palindromes found {len(pali_list)}")
print(*pali_list, sep='\n')

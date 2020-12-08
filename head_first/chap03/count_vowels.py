vowels = ['a', 'e', 'i', 'o', 'u']

word = input("put a word: ")

count_vowels = {}

for v in word:
    if v in vowels:
        if count_vowels.get(v) == None: 
            count_vowels[v] = 1
        else:
            count_vowels[v] += 1

print(count_vowels)


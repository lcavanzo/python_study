data = [ 1, 2, 3, 4, 5, 6, 7, 8 ]
evens = []
for num in data:
    if not num % 2:
        evens.append(num)
print(evens)

new_evens = [ num for num in data if num % 2 == 0]
print(new_evens)
print('------------------------------------------')

data = [ 1, 'one', 2, 'two', 3, 'three', 4, 'four' ]
words = []
for num in data:
    if isinstance(num, str):
        words.append(num)
print(words)

new_words = [ word for word in data if isinstance(word, str) ]
print(new_words)

print('------------------------------------------')
data = list('So long and thanks for all the fish'.split())
title = []
for word in data:
    title.append(word.title())

print(title)

new_title = [ word.title() for word in data ]
print(new_title)

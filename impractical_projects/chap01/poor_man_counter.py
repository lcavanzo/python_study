""" this program takes a string and return a simple bar chart"""

from collections import defaultdict

text = "Like the castle in its corner in a medieval game, I foresee "
text += "terrible trouble and I stay here just the same"
        
alphabet = defaultdict(list)

for letter in text.replace(" ", "").lower():
    alphabet.setdefault(letter, []).append(letter)

for k, v in sorted(alphabet.items()):
    print(f"{k}: {v}")

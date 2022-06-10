import json

filename = 'favorite_number.txt'

with open(filename) as f:
    favorite_number = json.load(f)

print(favorite_number)

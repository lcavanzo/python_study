import json

filename = 'favorite_number.txt'
favorite_number = input("What's your favorite number: ")

with open(filename, 'w') as f:
    json.dump(favorite_number, f)
print(f"I know your favorite number, Its {favorite_number}")

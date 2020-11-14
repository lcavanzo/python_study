import json

def get_stored_number():
    """Get stored number is it available"""
    filename = 'favorite_number.txt'
    try:
        with open(filename) as f:
            favorite_number = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return favorite_number

def get_new_number():
    """ask for a favorite number and validating"""
    try:
        favorite_number = int(input("What's your favorite number? "))
    except ValueError:
        print(f"You must put a number!!!")
    else:
        saving_number(favorite_number)


def saving_number(number):
    """Saving number into a json"""
    filename = 'favorite_number.txt'
    try:
        with open(filename, 'w') as f:
            json.dump(number, f)
    except FileNotFoundError:
        None
    else:
        print(f"I will remember your favorite number""")


def get_favorite_number():
    """show favorite number of the user"""
    favorite_number = get_stored_number()
    if favorite_number:
        print(f"Hello, Your favorite number is: {favorite_number}")
        answer = input(f"Is your favorite number? ")
        if answer == 'no':
            get_new_number()
        else:
            print(f":)")
    else:
        new_number = get_new_number()
get_favorite_number()

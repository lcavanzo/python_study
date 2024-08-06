import random


def get_guess():
    while True:
        guess = input("Guess the coin toss! Enter heads or tails: ").lower()
        if guess in ("heads", "tails"):
            return guess
        print("Invalid input. Please enter 'heads' or 'tails'!!")


def coin_toss():
    if random.randint(0, 1) == 0:
        return "tails"
    else:
        return "heads"


guess = get_guess()
toss = coin_toss()

if guess == toss:
    print("You got it")
else:
    print("Nope! Guess it again!!")
    toss = coin_toss()
    if guess == toss:
        print("You got it on the second try")
    else:
        print("Nope. You are really bad at this game")

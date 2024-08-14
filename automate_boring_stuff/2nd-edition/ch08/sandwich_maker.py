# sandwich_maker.py - program to order a sandwich
"""
Write a program that asks users for their sandwich preferences.
The program should use PyInputPlus to ensure that they enter valid input, such as:

Using inputMenu() for a bread type: wheat, white, or sourdough.
Using inputMenu() for a protein type: chicken, turkey, ham, or tofu.
Using inputYesNo() to ask if they want cheese.
If so, using inputMenu() to ask for a cheese type: cheddar, Swiss, or mozzarella.
Using inputYesNo() to ask if they want mayo, mustard, lettuce, or tomato.
Using inputInt() to ask how many sandwiches they want. Make sure this number is 1 or more.
Come up with prices for each of these options, and have your program display a total cost
after the user enters their selection.
"""

import pyinputplus as pyip

prices = {
    "bread_types": {"wheat": 1, "white": 2, "sourdough": 3},
    "protein_types": {"chicken": 4, "turkey": 5, "ham": 6, "tofu": 7},
    "cheese_types": {"cheddar": 1, "swiss": 2, "mozzarella": 3},
    "top_types": {"mayo": 4, "mustard": 5, "lettuce": 6, "tomato": 7},
}

# separate ingredients only
breads = list(prices["bread_types"].keys())
proteins = list(prices["protein_types"].keys())
cheese = list(prices["cheese_types"].keys())
top = list(prices["top_types"].keys())

flag = True
while flag:
    order = {}
    total_cash = 0
    print("Welcome, please, order your sandwich:\n")

    bread_response = pyip.inputMenu(
        prompt="What kind of bread do you want?\n", choices=breads
    )
    bread_cost = prices["bread_types"][bread_response]
    order[bread_response] = bread_cost
    protein_response = pyip.inputMenu(
        prompt="What kind of protein do you want?\n", choices=proteins
    )
    protein_cost = prices["protein_types"][protein_response]
    order[protein_response] = protein_cost
    has_cheese = pyip.inputYesNo(prompt="Do you want cheese?\n")
    if has_cheese.lower() == "yes":
        cheese_response = pyip.inputMenu(
            prompt="What kind of cheese do you want?\n", choices=cheese
        )
        cheese_cost = prices["cheese_types"][cheese_response]
        order[cheese_response] = cheese_cost
    has_top = pyip.inputYesNo(prompt="Do you want top?\n")
    if has_top.lower() == "yes":
        top_response = pyip.inputMenu(
            prompt="What kind of top do you want?\n", choices=top
        )
        top_cost = prices["top_types"][top_response]
        order[top_response] = top_cost
    total_sandwiches = pyip.inputInt(prompt="How many sandwiches do you want?: ", min=1)
    # order.append(total_sandwiches)
    for each_price in order.values():
        total_cash += each_price

    print(f"Total cost: ${total_cash*total_sandwiches}")

    flag = False

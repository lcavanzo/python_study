""" Attempt to make a lottery game"""
from random import choices


all_values = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 'a', 'b', 'c',
        'd','e')
winner_ticket = choices(all_values, k=4)

print(f"The winner ticket is: {winner_ticket}")

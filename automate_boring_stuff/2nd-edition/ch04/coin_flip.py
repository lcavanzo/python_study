# coin flip streaks
"""
Write a program to find out how often a streak of six heads or a streak of six tails
comes up in a randomly generated list of heads and tails
"""

import random

number_of_streaks = 0
flips = []
TOTAL_EXPERIMENTS = 10000

for experiment_number in range(TOTAL_EXPERIMENTS):
    # Code that creates a list of 100 'heads' or 'tails' values.
    for i in range(100):
        flip = random.randint(0, 1)
        flips.append("H" if flip == 1 else "T")

    # Code that checks if there is a streak of 6 heads or tails in a row.
    current_streak = 0
    current_side = None
    streak = False
    for flip in flips:
        if flip == current_side:
            current_streak += 1
            if current_streak == 6:
                streak = True
                current_streak = 0

        else:
            current_side = flip
            current_streak = 1
    if streak:
        number_of_streaks += 1

    flips.clear()

print(f"Chance of streak: {(number_of_streaks /  100)}%")

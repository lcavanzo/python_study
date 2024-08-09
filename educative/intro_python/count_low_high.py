"""
If a number is greater than 50 or divisible by 3, it will count as a high.
If these conditions are not met, the number is considered a low.

At the end of the function, you must return a list that contains the number of
lows and highs, in that order.

In case the list is empty, you may return None.

Sample Input
num_list = [20, 9, 51, 81, 50, 42, 77]
Sample Output
[2, 5] # 2 lows and 5 highs
"""


def get_lows_highs(n_list):
    if len(n_list) == 0:
        return None

    lows_highs = []
    lows = 0
    highs = 0
    for n in n_list:
        if n > 50 or n % 3 == 0:
            highs += 1
        elif n <= 50 and not n % 3 == 0:
            lows += 1
    lows_highs.append(lows)
    lows_highs.append(highs)
    return lows_highs


num_list = [20, 9, 51, 81, 50, 42, 77]
print(get_lows_highs(num_list))

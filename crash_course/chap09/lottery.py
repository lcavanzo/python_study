"""Playing lottery"""
from random import choice

lottery = [1, 2, 3, 4, 5,6,7,8,9,'a', 'b', 'c', 'd', 'e', ]
results = []
my_ticket = [8, 2, 2, 'a']
active = True
count = 0
while active:
    count += 1
    print(f"count #{count}")
    selected_option = choice(lottery)
    results.append(selected_option)
    if len(results) == 4:
        print(f"results: {results}")
        if my_ticket == results:
            print("##############################")
            print(f"my ticket {my_ticket}")
            print(f"results: {results}")
            print("You win")
            print("##############################")
            active = False
        else:
            results = []
        






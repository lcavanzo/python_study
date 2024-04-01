all_guests = {
    "Alice": {"apples": 5, "pretzels": 12},
    "Bob": {"ham sandwiches": 3, "apples": 2},
    "Carol": {"cups": 3, "apples pies": 1},
}


def total_brought(guests, item):
    total_item = 0
    for k, v in guests.items():
        total_item = total_item + v.get(item, 0)
    return total_item


print("Number of things being brought:")
print(" - Apples         " + str(total_brought(all_guests, "apples")))
print(" - Cups           " + str(total_brought(all_guests, "cups")))
print(" - Cakes          " + str(total_brought(all_guests, "cakes")))
print(" - Ham Sandwiches " + str(total_brought(all_guests, "ham sandwiches")))
print(" - Apple Pies     " + str(total_brought(all_guests, "apple pies")))

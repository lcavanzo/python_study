#The data structure to model the
## player’s inventory will be a dictionary where the keys are string values
## describing the item in the inventory and the value is an integer value
## detailing how many of that item the player has. For example, the diction-
## ary value {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
## means the player has 1 rope, 6 torches, 42 gold coins, and so on.
## Write a function named displayInventory() that would take any possible

def display_inventory(inventory_list):
    """Display the current player's inventory"""
    print("\tInventory")
    total_items = 0
    for item,amount in inventory_list.items():
        total_items += amount
        print(f"{amount} {item}")
    print(f"Total number of items: {total_items}")

def add_to_inventory(inventory_list, new_items):
    """Adding new items to the player's inventory"""
    for new_item in new_items:
        if new_item not in inventory_list.keys():
            inventory_list[new_item] = 1
        else:
            inventory_list[new_item] += 1
    return inventory_list


#stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
stuff = {'gold coin': 42, 'rope': 1}
dragon_loot = [
        'gold coin', 'dagger', 'dagger', 'gold coin',
        'dragon\'s armor', 'gold coin', 'ruby'
]
inv = add_to_inventory(stuff, dragon_loot)
display_inventory(inv)

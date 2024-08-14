# ff_game_inventory.
"""
You are creating a fantasy video game. The data structure to model the player’s inventory
will be a dictionary where the keys are string values describing the item in the inventory
and the value is an integer value detailing how many of that item the player has.
For example, the dictionary value
{'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
means the player has 1 rope, 6 torches, 42 gold coins, and so on.
"""


def display_inventory(inventory):
    """
    Displays the player's inventory
    """
    print("Inventory")
    item_total = 0
    for item, quantity in inventory.items():
        print(f"{quantity} {item}")
        item_total = item_total + quantity

    print(f"Total number of items: {item_total}")


def add_to_inventory(inventory, added_items):
    """
    Add item to the player's inventory
    """
    for item in added_items:
        if item in inventory:
            inventory[item] = inventory[item] + 1
        if item not in inventory:
            inventory.setdefault(item, 1)
    return inventory


# stuff = {"rope": 1, "torch": 6, "gold coin": 42, "dagger": 1, "arrow": 12}
inv = {"gold coin": 42, "rope": 1}
dragonLoot = ["gold coin", "dagger", "gold coin", "gold coin", "ruby"]
inv = add_to_inventory(inv, dragonLoot)
display_inventory(inv)

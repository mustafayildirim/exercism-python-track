from collections import Counter

def create_inventory(items):
    """

    :param items: list - list of items to create an inventory from.
    :return:  dict - the inventory dictionary.
    """

    return Counter(items)


def add_items(inventory, items):
    """

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return:  dict - the inventory dictionary update with the new items.
    """

    for item in items:
        if item in inventory.keys():
            value = inventory[item]
            value = value + 1
            inventory[item] = value
        else:
            inventory[item] = 1

    return inventory


def decrement_items(inventory, items):
    """

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return:  dict - updated inventory dictionary with items decremented.
    """

    items_to_decrement = Counter(items)
    for key in items_to_decrement:
        new_value = inventory[key] - items_to_decrement[key]
        if new_value >= 0:
            inventory[key] = new_value
        else:
            inventory[key] = 0

    return inventory


def remove_item(inventory, item):
    """
    :param inventory: dict - inventory dictionary.
    :param item: str - item to remove from the inventory.
    :return:  dict - updated inventory dictionary with item removed.
    """

    if item in inventory.keys():
        value = inventory.get(item)
        if value == 1:
            new_value = value - 1
            inventory[item] = new_value
        else:
            del inventory[item]

    return inventory


def list_inventory(inventory):
    """

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """

    final_inventory = []
    for key in inventory.keys():
        value = inventory[key]
        if value != 0:
            temp_record = (key, value)
            final_inventory.append(temp_record)

    return final_inventory

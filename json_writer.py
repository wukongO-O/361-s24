# CS361
# Shenglan Li
# Microsevice: text file (json) writer
# Description: get user input for a theater inventory list
#   (screens, seats, popcorn machine, ticket booth, self service ticket machine) and save the values to a json file.

from collections import defaultdict
import json

def main():
    inventory_items = ['screen', 'seat', 'popcorn machine', 'ticket booth', 'self-service ticket machine']
    inventory = defaultdict(dict)
    for item in inventory_items:
        inventory[item] = {
            'quantity': 0,
            'value': 0
        }

    print("Welcome to Theater Inventory Management Microservice.\n "
          "Please input the number and value of each inventory item:\n")

    # Get user input to populate the inventory
    current_item_idx = 0
    while current_item_idx < len(inventory_items):
        current_item = inventory_items[current_item_idx]
        try:
            quant = int(input(f"How many {current_item}s?\n"))
            inventory[current_item]['quantity'] = quant
        except ValueError:
            print("Please enter an integer.\n")
            continue

        current_done = 0
        while current_done != 1:
            try:
                cost = int(input(f"What is the value of the {current_item}s?\n"))
                inventory[current_item]['value'] = cost
                current_done = 1
                current_item_idx += 1
            except ValueError:
                print("Please enter an integer.\n")

    # Store values to a json file
    with open('inventory.json', 'w') as outfile:
        json.dump(inventory, outfile)


if __name__ == '__main__':
    main()
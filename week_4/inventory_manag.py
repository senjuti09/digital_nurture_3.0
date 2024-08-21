import threading
import time
import json

class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, item_name, quantity):
        if item_name in self.items:
            self.items[item_name] += quantity
        else:
            self.items[item_name] = quantity

    def remove_item(self, item_name, quantity):
        if item_name in self.items and self.items[item_name] >= quantity:
            self.items[item_name] -= quantity
        else:
            raise ValueError("Insufficient stock or item does not exist")

    def check_stock(self, item_name):
        return self.items.get(item_name, 0)

    def save_to_file(self, filename):
        try:
            with open(filename, 'w') as file:
                json.dump(self.items, file)
        except IOError as e:
            print(f"Error saving to file: {e}")

    def load_from_file(self, filename):
        try:
            with open(filename, 'r') as file:
                self.items = json.load(file)
        except IOError as e:
            print(f"Error loading from file: {e}")

    def restocking_alert(self, threshold=5):
        while True:
            for item, quantity in self.items.items():
                if quantity <= threshold:
                    print(f"Restocking Alert: {item} is low in stock with only {quantity} left.")
            time.sleep(10)

inventory = Inventory()
filename = input("Enter the inventory file name: ")
inventory.load_from_file(filename)

def manage_inventory():
    while True:
        action = input("Enter action (add/remove/exit): ")
        if action == "exit":
            inventory.save_to_file(filename)
            break
        item_name = input("Enter item name: ")
        quantity = int(input("Enter quantity: "))
        if action == "add":
            inventory.add_item(item_name, quantity)
        elif action == "remove":
            try:
                inventory.remove_item(item_name, quantity)
            except ValueError as e:
                print(e)

thread = threading.Thread(target=inventory.restocking_alert)
thread.daemon = True
thread.start()

manage_inventory()

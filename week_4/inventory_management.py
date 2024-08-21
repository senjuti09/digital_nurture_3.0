# inventory_management.py

# Lists
products = []

def add_product(product_name):
    products.append(product_name)

def remove_product(product_name):
    if product_name in products:
        products.remove(product_name)

def update_product(index, new_name):
    if 0 <= index < len(products):
        products[index] = new_name

# Dictionaries
product_details = {}

def add_product_details(name, quantity, price):
    product_details[name] = (quantity, price)

def update_product_details(name, quantity=None, price=None):
    if name in product_details:
        current_quantity, current_price = product_details[name]
        product_details[name] = (quantity if quantity is not None else current_quantity, 
                                 price if price is not None else current_price)

def delete_product_details(name):
    if name in product_details:
        del product_details[name]

# Tuples
def create_product_tuple(name, quantity, price):
    return (name, quantity, price)

def display_catalog(catalog):
    for product in catalog:
        print(product)

# Sets
categories = set()

def add_category(category):
    categories.add(category)

def remove_category(category):
    categories.discard(category)

# Combining Collections
def report_products_sorted_by_price():
    sorted_products = sorted(product_details.items(), key=lambda item: item[1][1])
    for name, (quantity, price) in sorted_products:
        print(f"Product: {name}, Quantity: {quantity}, Price: {price}")

def find_products_in_price_range(min_price, max_price):
    return {name for name, (quantity, price) in product_details.items() if min_price <= price <= max_price}

# Example usage
while True:
    action = input("Enter action (1. Add Product, 2. Remove Product, 3. Update Product, 4. Add Details, 5. Update Details, 6. Delete Details, 7. Add Category, 8. Remove Category, 9. Report by Price, 10. Find by Price Range, 11. Exit): ")
    if action == "1":
        product_name = input("Enter product name: ")
        add_product(product_name)
    elif action == "2":
        product_name = input("Enter product name to remove: ")
        remove_product(product_name)
    elif action == "3":
        index = int(input("Enter product index to update: "))
        new_name = input("Enter new product name: ")
        update_product(index, new_name)
    elif action == "4":
        name = input("Enter product name: ")
        quantity = int(input("Enter quantity: "))
        price = float(input("Enter price: "))
        add_product_details(name, quantity, price)
    elif action == "5":
        name = input("Enter product name to update: ")
        quantity = input("Enter new quantity (leave blank if no change): ")
        price = input("Enter new price (leave blank if no change): ")
        update_product_details(name, int(quantity) if quantity else None, float(price) if price else None)
    elif action == "6":
        name = input("Enter product name to delete: ")
        delete_product_details(name)
    elif action == "7":
        category = input("Enter category to add: ")
        add_category(category)
    elif action == "8":
        category = input("Enter category to remove: ")
        remove_category(category)
    elif action == "9":
        report_products_sorted_by_price()
    elif action == "10":
        min_price = float(input("Enter minimum price: "))
        max_price = float(input("Enter maximum price: "))
        products_in_range = find_products_in_price_range(min_price, max_price)
        print("Products in price range:", products_in_range)
    elif action == "11":
        break

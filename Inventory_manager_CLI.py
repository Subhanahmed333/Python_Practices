import csv

inventory = {}

def add_item(name, quantity, price):
    inventory[name] = {'quantity': quantity, 'price': price}
    print(f"{name} added with {quantity} units at Rs.{price} each.")

def sell_item(name, quantity):
    if name in inventory and inventory[name]['quantity'] >= quantity:
        inventory[name]['quantity'] -= quantity
        print(f"Sold {quantity} of {name}.")
    else:
        print("Not enough stock or item not found.")

def show_inventory():
    print("\n--- Inventory ---")
    for item, details in inventory.items():
        print(f"{item}: {details['quantity']} units @ Rs.{details['price']}")

def export_csv(filename="inventory.csv"):
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Item", "Quantity", "Price"])
        for name, data in inventory.items():
            writer.writerow([name, data['quantity'], data['price']])
    print(f"Inventory exported to {filename}")

# CLI loop
while True:
    print("\n1. Add Item  2. Sell Item  3. Show Inventory  4. Export  5. Exit")
    choice = input("Enter choice: ")

    if choice == '1':
        name = input("Item name: ")
        qty = int(input("Quantity: "))
        price = float(input("Price: "))
        add_item(name, qty, price)
    elif choice == '2':
        name = input("Item name: ")
        qty = int(input("Quantity to sell: "))
        sell_item(name, qty)
    elif choice == '3':
        show_inventory()
    elif choice == '4':
        export_csv()
    elif choice == '5':
        break
    else:
        print("Invalid choice.")

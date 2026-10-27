
# Restaurant Order Management System
# PS No. 31

menu = {
    "Burger": 100,
    "Pizza": 200,
    "Coffee": 50
}

tables = {i: [] for i in range(1, 21)}

print("====================================")
print("  RESTAURANT ORDER MANAGEMENT SYSTEM")
print("====================================")

print("\nMenu:")
for item, price in menu.items():
    print(f"{item}: Rs.{price}")

# Table validation
while True:
    try:
        table_no = int(input("\nEnter table number (1-20): "))

        if 1 <= table_no <= 20:
            break
        else:
            print("Invalid table number. Enter a number between 1 and 20.")

    except ValueError:
        print("Invalid table number. Enter a whole number.")

# Taking orders
while True:
    print("\nAvailable items:", ", ".join(menu.keys()))
    item = input("Enter order item (or 'done' to finish): ").strip().title()

    if item.lower() == "done":
        break

    if item not in menu:
        print("Item not on the menu. Available: Burger, Pizza, Coffee")
        continue

    try:
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Invalid quantity. Enter a positive whole number.")
            continue

    except ValueError:
        print("Invalid quantity. Enter a whole number.")
        continue

    # Add order to selected table
    tables[table_no].append({
        "item": item,
        "quantity": quantity,
        "price": menu[item]
    })

    amount = menu[item] * quantity

    print(f"{item} x{quantity} added to Table {table_no} | Amount: {amount}")

    # Show running order
    print("\nRunning Order:")
    for order in tables[table_no]:
        amount = order["price"] * order["quantity"]
        print(f'{order["item"]} x{order["quantity"]} = Rs.{amount}')

# Generate final bill
orders = tables[table_no]

if not orders:
    print("\nNo orders placed. Bill not generated.")
else:
    subtotal = 0

    print("\n====================================")
    print("             FINAL BILL")
    print("====================================")
    print(f"Table Number: {table_no}")
    print("------------------------------------")

    for order in orders:
        amount = order["price"] * order["quantity"]
        subtotal += amount
        print(
            f'{order["item"]} x{order["quantity"]} = Rs.{amount}'
        )

    service_charge = subtotal * 0.10
    gst = subtotal * 0.05
    total = subtotal + service_charge + gst

    print("------------------------------------")
    print(f"Subtotal: Rs.{subtotal:.2f}")
    print(f"Service Charge (10%): Rs.{service_charge:.2f}")
    print(f"GST (5%): Rs.{gst:.2f}")
    print("------------------------------------")
    print(f"TOTAL: Rs.{total:.2f}")
    print("====================================")
    print("Thank you for visiting!")

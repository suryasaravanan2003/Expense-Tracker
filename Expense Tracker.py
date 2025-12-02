expenses = []

def add_expense():
    amount = float(input("Enter amount: "))
    category = input("Enter category (Food, Travel, Shopping, Bills, Others): ")
    note = input("Enter note: ")
    expenses.append({"amount": amount, "category": category, "note": note})
    print("Expense added!\n")

def view_expenses():
    print("\n--- All Expenses ---")
    for e in expenses:
        print(f"{e['category']} - ₹{e['amount']} | {e['note']}")
    print()

def summary():
    print("\n--- Expense Summary ---")
    total = sum(e["amount"] for e in expenses)
    print(f"Total Spent: ₹{total}")

    categories = {}
    for e in expenses:
        categories[e["category"]] = categories.get(e["category"], 0) + e["amount"]

    for c, amt in categories.items():
        print(f"{c}: ₹{amt}")
    print()

while True:
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Summary")
    print("4. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        summary()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice\n")

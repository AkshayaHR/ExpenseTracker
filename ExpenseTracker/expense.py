expenses = []

def add_expense():
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")
    description = input("Enter description: ")
    expenses.append({
        "amount": amount,
        "category": category,
        "description": description
    })
    print("✅ Expense added!\n")

def view_expenses():
    print("\n📋 Expenses:")
    for e in expenses:
        print(f"{e['category']} - ₹{e['amount']} - {e['description']}")
    print()

while True:
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.\n")
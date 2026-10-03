
def delete_expense(expenses):
    if not expenses:
        print("No expenses available to delete.")
        return

    print("\n--- DELETE EXPENSE ---")

    for index, expense in enumerate(expenses, start=1):
        print(
            f"{index}. ₹{expense['Amount']} - "
            f"{expense['Category']} - "
            f"{expense['Description']}"
        )

    try:
        choice = int(input("Enter expense number to delete: "))

        if 1 <= choice <= len(expenses):
            del expenses[choice - 1]
            print("Expense deleted successfully.")
        else:
            print("Invalid expense number.")

    except ValueError:
        print("Please enter a valid number.")
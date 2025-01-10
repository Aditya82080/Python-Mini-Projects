import os

# File to save expense data
FILE_NAME = "expenses.txt"

def load_expenses():
    """Load expenses from file."""
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as file:
        return [line.strip().split(",") for line in file]

def save_expenses(expenses):
    """Save expenses to file."""
    with open(FILE_NAME, "w") as file:
        for expense in expenses:
            file.write(",".join(expense) + "\n")

def add_expense():
    """Add a new expense."""
    date = input("Enter the date (YYYY-MM-DD): ")
    description = input("Enter description: ")
    amount = input("Enter amount: ")
    category = input("Enter category: ")
    expenses.append([date, description, amount, category])
    save_expenses(expenses)
    print("Expense added successfully!")

def view_expenses():
    """View all expenses."""
    print("\nDate        | Description     | Amount | Category")
    print("-" * 50)
    for date, description, amount, category in expenses:
        print(f"{date:11} | {description:15} | {amount:6} | {category}")
    print()

def delete_expense():
    """Delete an expense."""
    view_expenses()
    try:
        idx = int(input("Enter the number of the expense to delete: ")) - 1
        if 0 <= idx < len(expenses):
            removed = expenses.pop(idx)
            save_expenses(expenses)
            print(f"Deleted: {removed}")
        else:
            print("Invalid index!")
    except ValueError:
        print("Invalid input!")

def main():
    print("Welcome to the Expense Tracker!")
    while True:
        print("\nOptions:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            delete_expense()
        elif choice == "4":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    expenses = load_expenses()
    main()

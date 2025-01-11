# Expense Tracker

## Description

The Expense Tracker is a Python application designed to help you manage and track your expenses effectively. With this program, you can easily add, view, and delete expenses, ensuring that your financial records are always organized. The data is stored persistently in a text file (expenses.txt) for future reference.

## Features

1. Add Expenses:

- Record expenses with details like date, description, amount, and category.

2. View Expenses:

- Display all recorded expenses in a tabular format for quick review.

3. Delete Expenses:

- Remove specific entries by selecting their index.

4. Persistent Storage:

- Automatically saves expenses to `expenses.txt`, ensuring your data remains available after restarting the application.

## Required Modules

This application uses Python's standard library and does not require any external modules.

## How to Install Required Modules

No additional modules need to be installed as the program only relies on Python’s built-in functionality. Ensure you have Python installed on your system (version 3.6 or above).

To check your Python version:
```
python --version
```
or
```
python3 --version
```
If Python is not installed, download it from python.org.

## How to Run the Script

1. Download the Script:

- Save the script as expense_tracker.py.

2. Run the Script:

- Open a terminal or command prompt.

- Navigate to the directory where `expense_tracker.py` is saved.

- Execute the script:
```
python expense_tracker.py
```
or
```
python3 expense_tracker.py
```

3. Using the Application:

- Follow the on-screen instructions to:

     - Add a new expense.

     - View the list of expenses.

     - Delete an expense by specifying its index.

- Exit the application when done. All data is saved automatically.


## Example Interaction
```bash
Welcome to the Expense Tracker!

Options:
1. Add Expense
2. View Expenses
3. Delete Expense
4. Exit

Enter your choice: 1
Enter the date (YYYY-MM-DD): 2025-01-09
Enter description: Grocery shopping
Enter amount: 50
Enter category: Food
Expense added successfully!

Options:
1. Add Expense
2. View Expenses
3. Delete Expense
4. Exit

Enter your choice: 2

Date        | Description     | Amount | Category
--------------------------------------------------
2025-01-09  | Grocery shopping|    50 | Food
```

## 
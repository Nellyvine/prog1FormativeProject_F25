
---

# Budget Tracker

A simple command-line budget tracking application built with Python. Users can record income and expenses, filter and view transactions, and see a summary of their budget. The application runs entirely in a single terminal session.

## Features

* **Add Transactions**: Record income or expenses with date, amount, category, and description
* **List Transactions**: Display all transactions in a clean, formatted table
* **Filter Transactions**: Filter by type, category, or month
* **Budget Summary**: View totals, balance, and spending breakdown by category
* **Input Validation**: Ensures correct date format, positive amounts, and valid menu choices
* **Session-Based Storage**: Data is stored in memory (not saved to a file)

## Requirements

* Python 3.x
* No external libraries required

## Installation

```bash
git clone https://github.com/Nellyvine/prog1FormativeProject_F25.git
cd prog1FormativeProject_F25
```

Ensure the following files are in the same directory:

* `main.py`
* `Budgettracker.py`
* `Transaction.py`

## Usage

Run the program from the terminal:

```bash
python main.py
```

## Menu Structure

```
Menu of the Budget Tracker
1) Add Income
2) Add Expense
3) List Transactions
4) Filter Transactions
5) Show Summary
0) Exit
```

## Sample Interactions

### Adding Income

```
Enter your choice from the menu above: 1

.......... Add Income...........
Enter the Date (YYYY-MM-DD) or press Enter for today: 2025-12-01
Enter the Amount: 5000
Enter the Category: Salary
Enter the Description: Monthly salary
Income Added
```

### Adding Expense

```
Enter your choice from the menu above: 2

.......... Add Expense...........
Enter the Date (YYYY-MM-DD) or press Enter for today: 2025-12-05
Enter the Amount: 150
Enter the Category: Groceries
Enter the Description: Weekly shopping
Expense Added
```

### Listing Transactions

```
Enter your choice from the menu above: 3

.......... List Transactions............
Date         | Type     | Amount     | Category        | Description
............................................................
2025-12-01   | income   | 5000.00    | salary          | Monthly salary
2025-12-05   | expense  | 150.00     | groceries       | Weekly shopping
```

### Filtering Transactions

```
Enter your choice from the menu above: 4

.......... Filter Transactions............
a) By type
b) By category
c) By month (YYYY-MM)
Choose option from (a, b, c): a
Enter the type (income/expense): expense

......... Filter Results ...............
Date         | Type     | Amount     | Category        | Description
............................................................
2025-12-05   | expense  | 150.00     | groceries       | Weekly shopping
```

### Viewing Summary

```
Enter your choice from the menu above: 5

.......... Budget Summary............
Total Income:   5000.0
Total Expense:  150.0
............................................................
Balance:        4850.0
............................................................
By Category:
SALARY : 5000.0
GROCERIES : 150.0
```

## Project Structure

The project uses object-oriented programming with the following classes:

* `Transaction`: Base class for any money movement
* `Income`: Subclass of `Transaction` for income entries
* `Expense`: Subclass of `Transaction` for expense entries
* `BudgetTracker`: Contains the transaction list and all core program functions

## Limitations

* Data is not saved after exiting
* No file export or persistent storage

## License

This project is for educational use only.

---




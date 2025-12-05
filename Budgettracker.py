from Transaction import *
from datetime import datetime

class BudgetTracker:
    # This class will hold list of transactions
    def __init__(self):
        self.transaction = []

    # Add income
    def add_income(self):
        print('\n.......... Add Income...........')
        date = self.get_date()
        amount = self.get_amount()
        category = input('Enter the Category: ')
        description = input('Enter the Description: ')
        income = Income(date, amount, category, description)
        self.transaction.append(income)
        print('Income Added')
        print('.' * 60)

    # Add expense
    def add_expense(self):
        print('\n.......... Add Expense...........')
        date = self.get_date()
        amount = self.get_amount()
        category = input('Enter the Category: ')
        description = input('Enter the Description: ')
        expense = Expense(date, amount, category, description)
        self.transaction.append(expense)
        print('Expense Added')
        print('.' * 60)

    # Print header for tables
    def print_head(self):
        print(f"{'Date':<12} | {'Type':<8} | {'Amount':<10} | {'Category':<15} | Description")
        print('.' * 60)

    # List all transactions
    def list_transactions(self):
        print('\n.......... List Transactions............')
        self.print_head()

        if not self.transaction:
            print('The list of transactions is empty now')
            return

        for t in self.transaction:
            print(f"{t.date:<12} | {t.type:<8} | {t.amount:<10.2f} | {t.category:<15} | {t.description}")
        print()

    # Filter transactions
    def filter_transactions(self):
        print("\n.......... Filter Transactions............")
        print("a) By type")
        print("b) By category")
        print("c) By month (YYYY-MM)")

        choice = input("Choose option from (a, b, c): ")


        if choice == "a":
            ttype = input("Enter the type (income/expense): ").lower()
            results = [t for t in self.transaction if t.type == ttype]

        elif choice == "b":
            cat = input("Enter the category: ").lower()
            results = [t for t in self.transaction if t.category.lower() == cat]

        elif choice == "c":
            month = input("Enter the month (YYYY-MM): ")
            results = [t for t in self.transaction if t.date.startswith(month)]

        else:
            print("Wrong option. Try again.")
            return

        print("\n......... Filter Results ...............")
        if not results:
            print("No matching transactions found for that filter.")
        else:
            self.print_head()
            for t in results:
                print(f"{t.date:<12} | {t.type:<8} | {t.amount:<10.2f} | {t.category:<15} | {t.description}")
        print()

    # Summary of budget
    def show_summary(self):
        print('\n.......... Budget Summary............')

        if not self.transaction:
            print('No data entry yet')
            return

        total_income = sum(t.amount for t in self.transaction if t.type == "income")
        total_expense = sum(t.amount for t in self.transaction if t.type == "expense")
        balance = total_income - total_expense

        print("Total Income:  ", total_income)
        print("Total Expense: ", total_expense)
        print('.' * 60)
        print("Balance:       ", balance)
        print('.' * 60)

        categories = {}
        for t in self.transaction:
            if t.category not in categories:
                categories[t.category] = 0
            categories[t.category] += t.amount

        print("By Category:")
        for c, amt in categories.items():
            print(c.upper(), ":", amt)

        print('.' * 60)

    # Get amount
    def get_amount(self):
        while True:
            index = input('Enter the Amount: ')
            try:
                index = float(index)
                if index <= 0:
                    print('Amount should be positive')
                else:
                    return index
            except:
                print('\nInvalid input. Try again')

    # Get date
    def get_date(self):
        while True:
            date_value = input('Enter the Date (YYYY-MM-DD) or press Enter for today: ')
            if not date_value:
                return datetime.now().strftime('%Y-%m-%d')

            try:
                datetime.strptime(date_value, '%Y-%m-%d')
                return date_value
            except:
                print('\nInvalid date format. Use YYYY-MM-DD format')

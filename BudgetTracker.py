
from datetime import datetime

class BudgetTracker:
#This class will hold list of transcations
    def __init__(self):
        self.transaction = []
#This is store all the transaction in a list

    def add_income(self):
        print('.......... Add Income...........')
        date = self.get_date()
        amount = self.get_amount()
        category = input('Enter the Category: ')
        description = input('Enter the Description: ')
        income = Income(date, amount, category, description) #creation of any object
        self.transaction.append(income)
        print('Income Added')
        print('.' *60)

    def add_expense(self):
        print('.......... Add Expense...........')
        date = self.get_date()
        amount = self.get_amount()
        category = input('Enter the Category: ')
        description = input('Enter the Description: ')
        expense = Expense(date, amount, category, description)
        self.transaction.append(expense)
        print('Expense Added')
        print('.' *60)

# This is a helper to print the table header so we don't repeat code
    def print_head(self):
        print(f"{'Date':<12} | {'Type':<8} |  {'Amount':<10} |{'Category':<15} | {'Description'}")
        print('.'*60)


#This shows all the transactions made
    def list_transactions(self):
        print('.......... List Transactions............')
        self.print_head()
        if not self.transaction:
            print('The list of transaction empty now')
            return
        for t in self.transaction:
            print(f"{t.date}:12 | {t.type:8} | {t.amount:8.2f} | {t.category:15} | {t.description}")
        print()

#This filters transactions
    def filter_transactions(self):
        self.print_head()
        print("--- Filter Transactions ---")
        print("a) By type")
        print("b) By category")
        print("c) By month (YYYY-MM)")
        choice = input("Choose option from (a,b,c): ")

       if choice == "a":
           ttype = input("Enter the type (income/expense): ").lower()
           results = [t for t in self.transaction if t.type == ttype]

       elif choice == "b":
           cat = input("Enter the category of the transaction: ").lower()
           results = [t for t in self.transaction if t.category == cat]

       elif choice == "c":
           month = input("Enter the month (YYYY-MM) of the transaction: ")
           results = [t for t in self.transaction if t.date.startswith(month)]

       else:
           print("Wrong option. Try again")
           return

    print(".........Filter Results...............")
    if not results:
        print("No matching transactions found with that filter.")
    else:
        for t in results:
            print(f"{t.date}:12 | {t.type:8} | {t.amount:8.2f} | {t.category:15} | {t.description}")
    print()

#This shows summary including total
    def show_summary(self):
        print('.......... Bugdet Summary............')
        if not self.transaction:
            print('No data entry yet')
            return

        total_income = sum(t.amount for t in self.transaction if t.type == "income")
        total_expense = sum(t.amount for t in self.transaction if t.type == "expense")
        balance = total_income - total_expense

        print('Total Income: ', + total_income)
        print('Total Expense: ', + total_expense)
        print('.' *60)
        print('Balance: ', + balance)

        categories = {}
        for t in self.transaction:
            if t.category not in categories:
                categories[t.category] = 0
            categories[t.category] += t.amount

        print('.'*60)
        print('By Category: ')
        for c, amt in categories.items():
            c = c.upper()
            print(c, amt)
        print()
        print('.' *60)

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
                print('Invalid input. Try again')

    def get_date(self):
        while True:
            date_value = input('Enter the Date (YYYY-MM-DD) or press Enter for today: ')
            if not date_value:
                return datetime.now().strftime('%Y-%m-%d')

            try:
                datetime.strptime(date_value, '%Y-%m-%d')
                return date_value
            except:
                print('Invalid date formate. Use YYYY-MM-DD format')










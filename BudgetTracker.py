class BudgetTracker:
#This class will hold list of transcations
    def __init__(self):
        self.transaction = []
#This is store all the transaction in a list
    def add_income(self):
        print('.......... Add Income...........')
        date = input('Enter Date (YYYY-MM-DD): ')
        amount = self.get_amount()
        category = input('Enter Category: ')
        description = input('Enter Description: ')
        income = Income(date, amount, category, description) #creation of any object
        self.transaction.append(income)
        print('Income Added')

    def add_expense(self):
        print('.......... Add Expense...........')
        date = input('Enter Date (YYYY-MM-DD): ')
        amount = self.get_amount()
        category = input('Enter Category: ')
        description = input('Enter Description: ')
        expense = Expense(date, amount, category, description)
        self.transaction.append(expense)
        print('Expense Added')

#This shows all the transactions made
    def list_transactions(self):
        print('.......... List Transactions............')
        if not self.transaction:
            print('No Transactions')
            return
        for t in self.transaction:
            print(t.date, t.amount, t.category, t.description)
        print()

#This filters transactions
    def filter_transactions(self):
        print("--- Filter Transactions ---")
        print("a) By type")
        print("b) By category")
        print("c) By month (YYYY-MM)")
        choice = input("Choose option(a,b,c: ")

       if choice == "1":
           ttype = input("Enter the type (income/expense): ").lower()
           results = [t for t in self.transaction if t.type == ttype]

       elif choice == "2":
           cat = input("Enter the category of the transaction: ").lower()
           results = [t for t in self.transaction if t.category == cat]

       elif choice == "3":
           month = input("Enter the month (YYYY-MM) of the transaction: ")
           results = [t for t in self.transaction if t.date.startswith(month)]

       else:
           print("Invalid filter option.")
           return

    print("--- Filter Results ---")
    if not results:
        print("No matching transactions found with that filter.")
    else:
        for t in results:
            print(f"{t.date} | {t.type.upper()} | {t.amount} | {t.category} | {t.description}")
    print()

#This shows summary including total
def show_summary(self):
        print('.......... Show Summary............')
        if not self.transaction:
            print('No data available')
            return

        total_income = sum(t.amount for t in self.transaction if t.type == "income")
        total_expense = sum(t.amount for t in self.transaction if t.type == "expense")
        balance = total_income - total_expense

        print('Total Income: ', + total_income)
        print('Total Expense: ', + total_expense)
        print('Balance: ', + balance)

        categories = {}
        for t in self.transaction:
            if t.category not in categories:
                categories[t.category] = 0
            categories[t.category] += t.amount

        print('by Category: ')
        for c, amt in categories.items():
            print(c, amt)
        print()

def get_amount(self):

        while True:
            index = input('Enter Amount: ')
            try:
                index = float(index)
                if index <= 0:
                    print('Amount should be positive')
                else:
                    return index
            except:
                print('Invalid input. Try again')


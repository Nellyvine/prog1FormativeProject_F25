#Transaction class(the parent class)

class Transaction:
    def __init__(self, date, amount, category, description,ttype):
        self.date = date
        self.amount = float(amount)
        self.category = category.lower().strip()
        self.description = description
        self.type = ttype #income/expense

class Income(Transaction):
#Child class inherited from parent
    def __init__(self, date, amount, category, description):
        super().__init__(date, amount, category, description, 'income')
#child class inherited from parent

class Expense(Transaction):
    def __init__(self, date, amount, category, description):
        super().__init__(date, amount, category, description, 'expense')




#Transaction class(the parent class)
class Transaction:
    def __init__(self, date, amount, category, description,ttype):
        self.date = date
        self.amount = float(amount)
        self.category = category
        self.description = description
        self.type = ttype #income/expense
class Income(Transaction):
    def __init__(self, date, amount, category, description):
        super().__init__(date, amount, category, description, 'income')

class Expense(Transaction):
    def __init__(self, date, amount, category, description):
        super().__init__(date, amount, category, description, 'expense')










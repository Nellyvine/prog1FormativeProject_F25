# This is the main menu and program loop

def main():
    bugdet = budgettracker()

    condition = True

    while condition:
        print(' Menu of the Budget Tracker')
        print('1) Add Income')
        print('2) Add Expense')
        print('3) List Transactions')
        print('4) Filter Transactions')
        print('5) Show Summary')
        print('0) Exit')

        choice = int(input('Enter your choice from the menu above: '))

        if choice == 1:
            bugdet.add_income()
        elif choice == 2:
            bugdet.add_expense()
        elif choice == 3:
            bugdet.list_transactions()
        elif choice == 4:
            bugdet.show_summary()
        elif choice == 5:
            bugdet.filter_transactions()
        elif choice == 0:
            print('Thank you for using BudgetTracker!')
            condition = False
        else:
            print('I did not understand that command, please try again.')

#This is to start the program

        if __name__ == '__main__':
            main()






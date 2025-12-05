from Budgettracker import BudgetTracker
# This is the main menu and program loop

def main():
    t = BudgetTracker()

    print('\nWelcome to BudgetTracker')
    print('\nTrack you Income and Expense with ease')

    condition = True

    while condition:


        print('\nMenu of the Budget Tracker')
        print('1) Add Income')
        print('2) Add Expense')
        print('3) List Transactions')
        print('4) Filter Transactions')
        print('5) Show Summary')
        print('0) Exit')
        print('.'*60)

        choice = int(input('\nEnter your choice from the menu above: '))

        if choice == 1:
            t.add_income()
        elif choice == 2:
            t.add_expense()
        elif choice == 3:
            t.list_transactions()
        elif choice == 4:
            t.filter_transactions()
        elif choice == 5:
            t.show_summary()
        elif choice == 0:
            print('\nThank you for using BudgetTracker')
            condition = False
        else:
            print('Wrong choice, please try again.')

#This is to start the program

if __name__ == '__main__':
    main()






from datetime import datetime,timedelta
from menu import show_menu

def calculate_total(expenses):
    print("======================")
    print("====CALCULATE TOTAL===")
    print("======================")
    print("1.Today")
    print("2.This Week")
    print("3.This Month")
    print("4.This Year")
    print("5.Back to Main Menu")
    choice = input("Choose an option :-")

    if choice == "1":
        print("TODAY'S EXPENSE TOTAL")
        today = datetime.now()
        found = False
        total = 0

        
        for expense in expenses:
            current = expense["Date"]
            if current.day == today.day and current.month == today.month and current.year == today.year:
               total = total + expense["Amount"]
               found = True
        print("TOTAL EXPENSE OF TODAY :-₹",total)

        if ( found == False):
            print("No expense for today.")

    elif choice == "2":
        today = datetime.now()
        start_of_the_week = today.date() - timedelta(days = today.weekday())
        total = 0 
        found = False

        for expense in expenses:
            current = expense["Date"].date()
            if start_of_the_week <= current <= today.date():
                total = total + expense["Amount"]
                found = True
        print("TOTAL EXPENSE OF THIS WEEK :-₹",total)

        if (found == False):
            print("No Expense of this Week.")

    elif choice == "3":
        today = datetime.now()
        total = 0 
        found = False

        for expense in expenses:
            current = expense["Date"]
            if current.month == today.month and current.year == today.year:
                total = total + expense["Amount"]
                found = True
        print("TOTAL EXPENSE OF THIS MONTH :-₹",total)

        if found == False:
            print("NO EXPENSE FOUND FOR THIS MONTH.")

    elif choice == "4":
        today = datetime.now()
        total = 0 
        found = False

        for expense in expenses:
            current = expense["Date"]
            if current.year == today.year:
                total = total + expense["Amount"]
                found = True
        print("TOTAL EXPENSE OF THIS YEAR :-₹",total)

        if found == False:
            print("NO EXPENSE FOUND FOR THIS YEAR")

    elif choice == "5":
        show_menu()

        

    return choice

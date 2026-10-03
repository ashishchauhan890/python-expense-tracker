from datetime import datetime

def add_expense(expenses):  
    print("ADD EXPENSE FUNCTION STARTED")
    choice = 1
    while ( choice == 1 ):
      expense = {
      "Amount": int(input("Enter the amount :- ")),
      "Category": input ("Enter the category :- "),
      "Description": input("Where you spend the money ?"),
      "Date": datetime.strptime(input("Enter the date (DD-MM-YYYY): "), "%d-%m-%Y")
      }
      expenses.append(expense)

      print(" Your Expense Added Successfully..")
      choice = int(input("Choose 1 to ADD ANOTHER EXPENSE OR Choose 2 to GO TO MAIN MENU :- "))
    return expenses
    

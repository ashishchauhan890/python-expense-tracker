from datetime import datetime,timedelta
from menu import show_menu


def view_expense(expenses):
  print("========================")
  print("     VIEW EXPENSE       ")
  print("========================")
  print("1.Today")
  print("2.This Week")
  print("3.This Month")
  print("4.This Year")
  print("5.Back to Main Menu")
  choice= input("Choose an option:- ")

  if  choice == "1" :
    print("EXPENSES OF TODAY...")

    today = datetime.now()
    found = False
    for expense in expenses:
      current = expense["Date"]
      if ( current.day == today.day and current.month == today.month and current.year == today.year):
        print("Amount :-",expense["Amount"])
        print("Category :-",expense["Category"])
        print("Description :-",expense["Description"])
        found = True
    if(found == False):
     print("No Expense for Today.")

  elif choice == "2": 
    print("THIS WEEK EXPENSE REPORT...")
  
 

    today = datetime.now()
    start_of_the_week = today.date() - timedelta(days=today.weekday())
    found = False

    for expense in expenses:
        current = expense["Date"].date()

        if start_of_the_week <= current <= today.date():
            
            print("Amount :-", expense["Amount"])
            print("Category :-", expense["Category"])
            print("Description :-", expense["Description"])
            print("Date :-", expense["Date"].strftime("%d-%m-%Y"))
            found = True

    if found == False:
        print("No Records found for this week.")
  
  

  elif(choice == "3"):
    print("THIS MONTH EXPENSE REPORT.")
    today = datetime.now()
    found = False

    for expense in expenses:
      current = expense["Date"]
      if current.month == today.month and current.year == today.year:
        print("Amount :-",expense["Amount"])
        print("Category :-",expense["Category"])
        print("Description :-",expense["Description"])
        print("Date :-",expense["Date"].strftime("%d-%m-%Y"))
        found = True
    if found == False:
      print("No Records found for this month.")

  elif(choice == "4"):
    print("THIS YEAR EXPENSE REPORT.")
    today = datetime.now()
    found = False

    for expense in expenses:
      current = expense["Date"]
      if current.year == today.year:
        print("Amount :-",expense["Amount"])
        print("Category :-",expense["Category"])
        print("Description :-",expense["Description"])
        print("Date :-",expense["Date"].strftime("%d-%m-%Y"))
        found = True
    if found == False:
      print("No Records found for this year.")

  elif(choice == "5"):
    show_menu()
          

  return choice
        

   

    



    
  

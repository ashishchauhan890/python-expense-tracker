import json
import os
from datetime import datetime
from menu import show_menu
from expense import add_expense
from reports import view_expense
from total_expense import calculate_total
from delete_expense import delete_expense
from budget import set_budget,check_budget,save_budget,load_budget


def save_expenses(expenses):
    data = []

    for expense in expenses:
        item = expense.copy()
        item["Date"] = item["Date"].strftime("%d-%m-%Y")
        data.append(item)

    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)

if os.path.exists("data.json"):
    with open("data.json", "r") as file:
        expenses = json.load(file)

    for expense in expenses:
        expense["Date"] = datetime.strptime(
            expense["Date"], "%d-%m-%Y"
        )
else:
    expenses = []

monthly_budget = load_budget()

while True:
  choice = show_menu()

  print("You selected:", choice)

  if choice == "1":
    expenses = add_expense(expenses)
    save_expenses(expenses)

  elif choice == "2":
    view_expense(expenses)

  elif choice == "3":
    calculate_total(expenses)

  elif choice == "4":
    delete_expense(expenses)
    save_expenses(expenses)

  elif choice == "5":
      monthly_budget = set_budget()
      check_budget(monthly_budget , expenses)
      save_budget(monthly_budget)

  elif choice == "6":
    print("Exit from Expense Tracker.")
    break


    



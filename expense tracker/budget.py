from datetime import datetime
import json
import os

def set_budget():
    budget = int(input("SET MONTHLY BUDGET :-"))
    return budget

def calculate_monthly_spending(expenses):
    today = datetime.now()
    total = 0 
    for expense in expenses:
        current = expense["Date"]
        if current.month == today.month and current.year == today.year:
            total = total + expense["Amount"]
    print("THIS MONTH TOTAL EXPENSE :-₹",total)
    return total

def check_budget(budget,expenses):
    total = calculate_monthly_spending(expenses)
    remaining = budget - total

    print("MONTHLY BUDGET :-",budget)
    print("TOTAL SPEND :-",total)
    print("REMAINING BUDGET :-",remaining)

    if remaining < 0:
        print("You have exceeded Monthly limit.")
    else:
        print("Your Expenses are within budget limit.")



def save_budget(budget):
    data = {
        "monthly_budget": budget
    }

    with open("budget.json", "w") as file:
        json.dump(data, file, indent=4)

    print("Monthly budget saved successfully.")


def load_budget():
    if os.path.exists("budget.json"):
        with open("budget.json", "r") as file:
            data = json.load(file)
            return data["monthly_budget"]
    else:
        return 0



     


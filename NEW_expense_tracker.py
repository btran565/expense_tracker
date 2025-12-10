################
#FOR TESTING
################

import sys, os, json
import argparse
from datetime import datetime, date

data_folder = "data"    
os.makedirs(data_folder, exist_ok=True)

file_path = os.path.join(data_folder, 'expenses.json')
if not os.path.exists(file_path):
    # Create an empty expenses.json file if it doesn't exist
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump([], f)    #initialize as empty list ()

parser = argparse.ArgumentParser()
subparsers = argparse.add_subparsers()

parser.add_argument('action', help='actions: add, update, delete, list, summary') #positional argument
parser.add_argument('--date', default=date.today().strftime("%Y-%m-%d"), type=str, help='date of expense (YYYY-MM-DD), current date used if not specified')
parser.add_argument('--description', type=str, help = 'description of expense') #optional arguments
parser.add_argument('--amount', type=float, help = 'amount of expense')
parser.add_argument('--id', type=int, help = 'id number of expense')
parser.add_argument('--month', type=int, help = 'month of summary')

args = parser.parse_args()

def load_expenses():    #reads json and returns data list
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data

def args_check(expenses):   #error handling for missing/invalid arguments
    if args.action == 'add':
        if args.description == None or args.amount == None:
            print("Error: the action 'add' requires arguments: --date, --description, --amount")
            return False
        if check_date(args.date) == False:
            return False
        if args.amount < 0:
            print("Error: the amount for this expense must be a positive value")
            return False
    if args.action == 'update':
        if args.id == None:
            print("Error: the action 'update' requires argument: --id")
            return False
        try:
            id_check = expenses[args.id - 1]
        except IndexError:
            print(f"Error: an expense with ID {args.id} does not exist")
            return False
        if args.date == None and args.description == None and args.amount == None:
            print(f"Error: one of the following arguments are required to update Expense ID: {args.id}: --date, --description, --amount")
            return False
        if check_date(args.date) == False:
            return False
        if args.amount < 0:
            print("Error: the amount for this expense must be a positive value")
            return False
    if args.action == 'delete':
        if args.id == None:
            print("Error: the action 'delete' requires argument: --id")
            return False
        try:
            id_check = expenses[args.id -1]
        except IndexError:
            print(f"Error: an expense with ID {args.id} does not exist")
            return False
    if args.action == 'summary':
        if args.month:
            if args.month < 1 or args.month > 12:
                print("Error: the 'month' argument must be a valid month from 1 to 12")
                return False
    return True

def to_file(expenses):  #writes expenses list to json
    with open(file_path, 'w') as f:
        json.dump(expenses, f, indent=4)
    return

def check_date(date_str):    #changes date string from arg value into date obj
    try:
        date_check = datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        print("Date format must be YYYY-MM-DD.")
        return False

def add_data(expenses):  #takes list of args and appends it into a dict of dicts. each dict has a int key and dict value
    new_id = len(expenses) + 1
    expenses.append({    #saves date as str in JSON
        "date": args.date, 
        "description": args.description, 
        "amount": args.amount
    })
    
    to_file(expenses)
    print(f"Expense added successfully (ID: {new_id})")
    return 

def update_data(expenses):    #checks optional args date/desc/amt and updates expense with provided id
    id = args.id -1
    if args.date:
        expenses[id].update({"date": args.date})
    if args.description:
        expenses[id].update({"description": args.description})
    if args.amount:
        expenses[id].update({"amount": args.amount})
    to_file(expenses)
    print("Expense updated successfully")
    return

def delete_data(expenses): #delete expense by popping list
    del expenses[args.id-1]
    to_file(expenses)
    print(f"Expense deleted successfully. Use the 'list' action to view updated expense ID's")
    return 

def list_data(expenses):
    print(f"{'ID':<3} {'Date':<10} {'Description':<40} {'Amount':<6}")
    for id, e in enumerate(expenses, start=1):
        print(f"{id:<3} {e['date']:<10} {e['description']:<40} {e['amount']:<6}")
    return

def summary_data(expenses):
    e_sum = 0
    if args.month:  #if 'month' argument is entered, summary of monthly expense will be printed
        for e in expenses:
            date_obj = datetime.strptime(e['date'], "%Y-%m-%d")
            if date_obj.month == args.month:
                e_sum += e['amount']
            month_name = date_obj.strftime("%B")
        print(f"Total expenses for {month_name}: ${e_sum}")
        return
    else:
        for e in expenses:
            e_sum += e['amount']
        print(f"Total expenses: ${e_sum}")
    return

def clear_list(expenses):   #clears expenses list and JSON file
    expenses.clear()
    to_file(expenses)
    print("List of expenses cleared.")

def main():
    #functionality 
    expenses = load_expenses()
    if args_check(expenses):
        if args.action == "exit":
            print("Exiting the Expense Tracker.")
            sys.exit(0)
        if args.action == "clear":
            clear_list(expenses)
        if args.action == "add":
            add_data(expenses)
        if args.action == "update":
            update_data(expenses)
        if args.action == "delete":
            delete_data(expenses)        
        if args.action == "list":
            list_data(expenses)
        if args.action == "summary":
            summary_data(expenses)
    else:
        print("Invalid argument(s). Exiting expense_tracker.py")
        sys.exit(0)


if __name__ == '__main__':
    main()
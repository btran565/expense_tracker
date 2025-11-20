import sys, os, json
import argparse
from datetime import date

data_folder = "data"    
os.makedirs(data_folder, exist_ok=True)

file_path = os.path.join(data_folder, 'expenses.json')
if not os.path.exists(file_path):
    # Create an empty expenses.json file if it doesn't exist
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump([], f)

parser = argparse.ArgumentParser()


parser.add_argument('action', help='choose from the following actions: add, update, delete, list, or summarize') #positional argument
parser.add_argument('--date', default=None, type=str, help='date of expense (YYYY-MM-DD), current date used if not specified')
parser.add_argument('--description', type=str, help = 'description of expense') #optional arguments
parser.add_argument('--amount', type=float, help = 'amount of expense')
parser.add_argument('--id', type=int, help = 'id number of expense')
args = parser.parse_args()

def load_expenses():    #reads json and returns data list
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data

def args_check():
    if args.action == 'add':
        if args.date == None or args.description == None or args.amount == None:
            print("Error: the action 'add' requires arguments: --date, --description, --amount")
            return False
    if args.action == 'update':
        if args.id == None:
            print("Error: the action 'update' requires argument: --id")
            return False
        if args.date == None and args.description == None and args.amount == None:
            print(f"Error: one of the following arguments are required to update Expense ID: {args.id}: --date, --description, --amount")
            return False
    if args.action == 'delete':
        if args.id == None:
            print("Error: the action 'delete' requires argument: --id")
            return False
    else:
        return True

def to_file(expenses):  #writes expenses list to json
    with open(file_path, 'w') as f:
        json.dump(expenses, f, indent=4)
    return

def check_date(date_str):    #changes date string from arg value into date obj MIGHT DELETE
    try:
        date_check = date.fromisoformat(date_str) #checks if date_str can be formatted into a date obj
    except ValueError:
        print("Date format must be YYYY-MM-DD.")
    return date_str

def add_data(expenses):  #wIP takes list of args and appends it into a dict of dicts. each dict has a int key and dict value
    new_id = len(expenses) + 1
    expenses[new_id] = {     
        "date": args.date, 
        "description": args.description, 
        "amount": args.amount
    }
    
    to_file(expenses)
    print(f"Expense added successfully (ID: {new_id})")
    return 

def update_data(expenses):    #for loop iterating thru expense element dict WIP
    
    return

def delete_data(id, expenses): #(int) delete expense by popping list
    del expenses[id]
    print(f"Expense deleted successfully")
    return 

def list_data():
    return

def summary_data():
    return

def month_summary_data():
    return



def main():
    #functionality 
    expenses = load_expenses()
    if args_check():
        if args.action == "exit":
            print("Exiting the Expense Tracker.")
            sys.exit(0)
        if args.action == "add":
            ###new_date = check_date(args.date) #might not be needed
            add_data(expenses)
        if args.action == "update":
            update_data(expenses)
        if args.action == "delete":
            delete_data(args.id, expenses)        
    else:
        sys.exit(0)


if __name__ == '__main__':
    main()
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
parser.add_argument('--date', default=date.today().isoformat(), type=str, help='date of expense (YYYY-MM-DD), current date used if not specified')
parser.add_argument('--description', default='no description given', type=str, help = 'description of expense') #optional arguments
parser.add_argument('--amount', default=0.00, type=float, help = 'amount of expense')
parser.add_argument('--id', default=0, type=int, help = 'id number of expense')
args = parser.parse_args()

def load_expenses():    #reads json and returns data
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data

def check_args():
    return

def to_file(expenses):  #writes expenses list to json
    with open(file_path, 'w') as f:
        json.dump(expenses, f, indent=4)
    return

def add_data(arg_list, expenses):  #wIP takes list of args and appends it into a dict of dicts. each dict has a int key and dict value
    new_id = len(expenses) + 1
    expenses[new_id] = {     
        "date": arg_list[0], 
        "description": arg_list[1], 
        "amount": arg_list[2]
    }
    
    to_file(expenses)
    print(f"Expense added successfully (ID: {new_id})")
    return 

def update_data(id, expenses):    #for loop iterating thru expense element dict WIP
    
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

def check_date(date_str):    #changes date string from arg value into date obj
    try:
        date_check = date.fromisoformat(date_str) #checks if date_str can be formatted into a date obj
    except ValueError:
        print("Date format must be YYYY-MM-DD.")
    return date_str

def main():
    #functionality 
    print("Welcome to the expense tracker. Type --h for the list of commands.")
    expenses = load_expenses()
    #while True:
    if args.action == "exit":
        print("Exiting the Expense Tracker.")
        sys.exit(0)
    if args.action == "add":
        new_date = check_date(args.date)
        add_data([new_date, args.description, args.amount], expenses)
    if args.action == "update":
        update_data([args.date, args.description, args.amount], expenses)
    if args.action == "delete":
        delete_data(args.id, expenses)        
   


if __name__ == '__main__':
    main()
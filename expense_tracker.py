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


parser.add_argument('action', help='choose from the following actions: add, update, delete, view, or summarize') #positional argument
parser.add_argument('--date', default=date.today().isoformat(), type=str, help='date of expense (YYYY-MM-DD), current date used if not specified')
parser.add_argument('--description', default='no description given', type=str, help = 'description of expense') #optional arguments
parser.add_argument('--amount', default=0.00, type=float, help = 'amount of expense')
parser.add_argument('--id', default=0, type=int, help = 'id number of expense')
args = parser.parse_args()

expenses = {}   #global dict of dicts

def read_file(): # reads json and returns data WIP?
    with open(file_path, 'r') as f:
        data = json.load(f)
        print(f'{data[0]}')    #WIP
    return data

def to_file(list):  #writes expenses list to json
    with open(file_path, 'w') as f:
        json.dump(expenses, f, indent=4)
    return

def update_expenses(data):
    

    return  #WIP

def add_data(new_expense):  #wIP takes list of args and appends it into a list of dicts. each dict has a int key and dict value
    new_id = len(expenses) + 1
    expenses =  {   #dict of dict
        new_id: 
            {
                "date": new_expense[0], 
                "description": new_expense[1], 
                "amount": new_expense[2]
            }
    }
    to_file(expenses)
    print(f"Expense added successfully (ID: {new_id})")
    return 

def update_data(id):    #for loop iterating thru expense element dict WIP
    
    return

def delete_data(id): #(int) delete expense by popping list
    expenses.pop(id)
    print(f"Expense deleted successfully")
    return 

def check_date(date_str):    #changes date string from arg value into date obj
    try:
        date_check = date.fromisoformat(date_str) #checks if date_str can be formatted into a date obj
    except ValueError:
        print("Date format must be YYYY-MM-DD.")
    
    
    
    return date_str

def check_for_data():
    return  #WIP checks JSON

def main():
    #functionality 
    print("Welcome to the expense tracker. Type --h for the list of commands.")
    read_file()
    #while True:
    if args.action == "exit":
        print("Exiting the Expense Tracker.")
        sys.exit(0)
    if args.action == "add":
        new_date = check_date(args.date)
        add_data([new_date, args.description, args.amount])        
   


if __name__ == '__main__':
    main()
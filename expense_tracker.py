import sys, os, json
import argparse
from datetime import date

data_folder = "expense_tracker/data"    
os.makedirs(data_folder, exist_ok=True)

parser = argparse.ArgumentParser()


parser.add_argument('action', help='choose from the following actions: add, update, delete, view, or summarize') #positional argument
parser.add_argument('--date', default=date.today(), help='date of expense (YYYY-MM-DD), current date used if not specified')
parser.add_argument('--description', default='no description given', type=str, help = 'description of expense') #optional arguments
parser.add_argument('--amount', default=0.00, type=float, help = 'amount of expense')
parser.add_argument('--id', default=0, type=int, help = 'id number of expense')
args = parser.parse_args()

expenses = []

def read_file(): #reads csv of existing expenses and saves it to expenses[]
    with open('expense_tracker/data/expenses.json', 'r') as file:
        data = json.load(file)
    return

def to_file(list):
    with open('expense_tracker/data/expenses.json', 'w', ) as file:
        for expense in list:
            json.dump(expense, file, indent=4)

        '''
        csv_writer = csv.writer(file)
        for expense in list:
            print(f"{expense}")
            csv_writer.writerow([expense])
            '''
    return

def add_data(new_expense):  #takes list of args and appends it into a list of dicts. each dict has a int key and dict value
    new_id = len(expenses) + 1
    expenses.append(
        {
            new_id: 
            {
                "date": new_expense[0], 
                "description": new_expense[1], 
                "amount": new_expense[2]
            }
        })
    to_file(expenses)
    print(f"Expense added successfully (ID: {new_id})")
    return 

def update_data(id):    #for loop iterating thru expense element dict
    
    return

def delete_data(id): #(int) delete expense by popping list
    expenses.pop(id)
    print(f"Expense deleted successfully")
    return 

def to_date(date_str):    #changes date string from arg value into date obj
    date_obj = date.fromisoformat(date_str) #somethings wrong
    return date_obj

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
        new_date = to_date(args.date)
        add_data([new_date, args.description, args.amount])        
   


if __name__ == '__main__':
    main()
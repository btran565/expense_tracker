import sys
import argparse
from datetime import date

parser = argparse.ArgumentParser()


parser.add_argument('action', help='choose from the following actions: add, update, delete, view, or summarize') #positional argument
parser.add_argument('--date', default=date.today(), help='date of expense (YYYY-MM-DD), current date used if not specified')
parser.add_argument('--description', default='no description given', type=str, help = 'description of expense') #optional arguments
parser.add_argument('--amount', default=0.00, type=float, help = 'amount of expense')
args = parser.parse_args()

expenses = []

def add_data(expense):  #WIP

    return id

def edit_data(action, id): #(str, int) update or delete functionality
    return #WIP

def to_date(date_str):    #changes date string from arg value into date obj
    date_obj = date.fromisoformat(date_str)
    return

#def get_id():

def check_for_data():
    return  #WIP checks JSON

def main():
    #functionality 
    if args.action == "add":
        
        edit_data(args.action, [args.date, args.description, args.amount])
        print(f"added expense: date:{args.date} desc:{args.description}  amount:${args.amount}")
        
   


if __name__ == '__main__':
    main()
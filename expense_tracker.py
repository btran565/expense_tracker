import sys
import argparse
from datetime import date

parser = argparse.ArgumentParser()

parser.add_argument('action', help='choose from the following actions: add, update, delete, view, or summarize') #positional argument
parser.add_argument('--date', default=date.today(), help='date of expense (YYYY/MM/DD), current date used if not specified')
parser.add_argument('--description', default='no description given', type=str, help = 'description of expense') #optional arguments
parser.add_argument('--amount', default=0.00, type=float, help = 'amount of expense')
args = parser.parse_args()

expenses = []
def edit_data(action, expense): #(integer, list)
    return

def check_for_data():
    return  #WIP

def main():
    #functionality 
    if args.action == "add":
        edit_data(args.action, [args.date, args.description, args.amount])
        print(f"added {args.description} and ${args.amount}")
        
   


if __name__ == '__main__':
    main()
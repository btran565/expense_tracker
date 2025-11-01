import sys
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('action', help='action to add, update, delete, view, or summarize')
"""
parser.add_argument('add', help='add an expense')  #positional arguments
parser.add_argument('update', help='update an existing expense')
parser.add_argument('delete', help='delete an existing expense')
parser.add_argument('view', help='view all existing expenses')
parser.add_argument('summarize', help='summarize all expenses')
"""
    
parser.add_argument('--description', metavar='no description given', type=str, help = 'description of expense')    #optional arguments
parser.add_argument('--amount', metavar=0.00, type=float, help = 'amount of expense')
args = parser.parse_args()


expenses = []
def add_expense(expenses):
    expenses.add[parser.description]

def main():

    #functionality 
    if args.action == "add":
        print(f"added {args.description} and {args.amount}")
        
   


if __name__ == '__main__':
    main()
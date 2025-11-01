import sys
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('action', help='choose from the following actions: add, update, delete, view, or summarize') #positional argument
parser.add_argument('--description', default='no description given', type=str, help = 'description of expense') #optional arguments
parser.add_argument('--amount', default=NULL, type=float, help = 'amount of expense')
args = parser.parse_args()


expenses = []
def add_expense(expenses):
    expenses.add[parser.description]

def check_for_data():
    return  #WIP

def main():

    #functionality 
    if args.action == "add":
        print(f"added {args.description} and {args.amount}")
        
   


if __name__ == '__main__':
    main()
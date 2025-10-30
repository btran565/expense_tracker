import sys
import argparse
from datetime import date

expenses = []

def add_expense():
    
    return

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('add', help='add an expense')  #positional arguments
    parser.add_argument('update', help='update an existing expense')
    parser.add_argument('delete', help='delete an existing expense')
    parser.add_argument('view', help='view all existing expenses')
    parser.add_argument('summarize', help='summarize all expenses')
    
    parser.add_argument('--description', type=str, help = 'description of expense')    #optional arguments
    parser.add_argument('--amount', type=int, help = 'amount of expense')
    args = parser.parse_args()

    #functionality below
    if args.add:
        print('You want to add an expense?')

if __name__ == '__main__':
    main()
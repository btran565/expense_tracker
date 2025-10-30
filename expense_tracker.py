import sys
import argparse
from datetime import date

expenses = []

def add_expense():
    
    return

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('add', help='add an expense')  #positional argument
    parser.add_argument('--description', type=str, help = 'description of expense')    #optional argument
    parser.add_argument('--amount', type=int, help = 'amount of expense')
    args = parser.parse_args()

    #functionality below


    print(f"Hi! Thanks for entering your name.")

if __name__ == '__main__':
    main()
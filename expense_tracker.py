import sys
import argparse
from datetime import date

expenses = []

def add_expense():
    
    return

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('add', type=int, help='add an expense')  #positional argument
    parser.add_argument('--description', type=str, help = 'description of expense')    #optional argument
    parser.add_argument('--amount', type=str, help = 'amount of expense')
    args = parser.parse_args()

    print(f"Hi {args.name}! Thanks for entering your name.")

main()
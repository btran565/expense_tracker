import sys
import argparse
from datetime import date

expenses = []

def add_expense():
    
    return

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("name")
    args = parser.parse_args()

    print(f"Hi {args.name}! Thanks for entering your name.")

main()
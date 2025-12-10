from datetime import datetime, date

def check_add(expenses, args):
    if args.description == None or args.amount == None:
            print("Error: the action 'add' requires arguments: --date, --description, --amount")
            return False
    if check_date(args.date) == False:
            return False
    if args.amount < 0:
            print("Error: the amount for this expense must be a positive value")
            return False

def check_update(expenses, args):
    pass

def check_delete(expenses, args):
    pass

def check_summary(expenses, args):
    pass


from datetime import datetime, date
from utils import check_date


def check_add(args):
    if args.description == None or args.amount == None:
            print("Error: the action 'add' requires arguments: --date, --description, --amount")
            return False
    if check_date(args.date) == False:
            return False
    if args.amount < 0:
            print("Error: the amount for this expense must be a positive value")
            return False

def check_update(expenses, args):

    if args.id == None:
            print("Error: the action 'update' requires argument: --id")
            return False
    try:
        id_check = expenses[args.id - 1]
    except IndexError:
        print(f"Error: an expense with ID {args.id} does not exist")
        return False
    if args.date == None and args.description == None and args.amount == None:
        print(f"Error: one of the following arguments are required to update Expense ID: {args.id}: --date, --description, --amount")
        return False
    if check_date(args.date) == False:
        return False
    if args.amount < 0:
        print("Error: the amount for this expense must be a positive value")
        return False

def check_delete(expenses, args):
    if args.id == None:
        print("Error: the action 'delete' requires argument: --id")
        return False
    try:
        id_check = expenses[args.id -1]
    except IndexError:
        print(f"Error: an expense with ID {args.id} does not exist")
        return False

def check_summary(expenses, args):
    e_sum = 0
    if args.month:  #if 'month' argument is entered, summary of monthly expense will be printed
        for e in expenses:
            date_obj = datetime.strptime(e['date'], "%Y-%m-%d")
            if date_obj.month == args.month:
                e_sum += e['amount']
            month_name = date_obj.strftime("%B")
        print(f"Total expenses for {month_name}: ${e_sum}")
        return
    else:
        for e in expenses:
            e_sum += e['amount']
        print(f"Total expenses: ${e_sum}")
    return


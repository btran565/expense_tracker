import sys, os, json
import argparse
from datetime import datetime, date
import tools.action_add as add_obj
import tools.action_update as update_obj
import tools.action_delete as delete_obj
import tools.action_list as list_obj
import tools.action_summary as summary_obj
import tools.utils as utils

# TODO: move to utils or separate data layer
data_folder = "data"    
os.makedirs(data_folder, exist_ok=True)

file_path = os.path.join(data_folder, 'expenses.json')
if not os.path.exists(file_path):
    # Create an empty expenses.json file if it doesn't exist
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump([], f)    #initialize as empty list ()

parser = argparse.ArgumentParser()
#parser.add_argument('action', help='actions: add, update, delete, list, summary') #positional argument
subparsers = parser.add_subparsers(dest='action', help='actions: add, update, delete, list, summary')

parser_add = subparsers.add_parser('add', help='Add a new expense')
parser_add.add_argument('--date', type=str, help='date of expense (YYYY-MM-DD), current date used if not specified')
parser_add.add_argument('--description', required = True, type=str, help = 'description of expense') #optional arguments
parser_add.add_argument('--amount', required = True, type=float, help = 'amount of expense')

parser_update = subparsers.add_parser('update', help='Update an existing expense')
parser_update.add_argument('--id', required=True, type=int, help = 'id number of expense')
parser_update.add_argument('--date', type=str, help='date of expense (YYYY-MM-DD), current date used if not specified')
parser_update.add_argument('--description', type=str, help = 'description of expense') #optional arguments
parser_update.add_argument('--amount', type=float, help = 'amount of expense')

parser_delete = subparsers.add_parser('delete', help='Deletes an existing expense')
parser_delete.add_argument('--id', required=True, type=int, help = 'id number of expense')

parser_list = subparsers.add_parser('list', help='Lists all existing expenses')

parser_summary = subparsers.add_parser('summary', help="Returns a sum of all expenses or all expenses in a month if the argument '--month' is used")
parser.add_argument('--month', type=int, help = 'month of summary')

args = parser.parse_args()


def main():
    #functionality 
    file_path = utils.init_file_path()
    expenses = utils.load_expenses(file_path)
    check = None

    match args.action:
        case "exit":
            print("Exiting the Expense Tracker.")
            sys.exit(0)
        case "clear":
            utils.clear_list(expenses, file_path)
        case "add":
            check = add_obj.Add().validate(args)
            if check:
                add_obj.Add().run(expenses, args, file_path)
        case "update":
            check = update_obj.Update().validate(expenses, args)
            if check:
                update_obj.Update().run(expenses, args, file_path)
        case "delete":
            check = delete_obj.Delete().validate(expenses, args)
            if check:
                delete_obj.Delete().run(expenses, args, file_path)
        case "list":
            check = list_obj.List().validate(expenses)
            if check:
                list_obj.List().run(expenses)
                sys.exit(0)
        case "summary":
            check = summary_obj.Summary().validate(expenses, args)    
            if check:    
                summary_obj.Summary().run(expenses, args)
                sys.exit(0)

    if check == False:        
        print("Invalid argument(s). Exiting expense_tracker.py")
        sys.exit(0)


if __name__ == '__main__':
    main()
import sys
from tools.action_base import Action
from tools.utils import check_date, to_file

class Update(Action): 

    def validate(self, expenses, args):
        try:
            test = expenses[0]
        except IndexError:
            print("Notice: There are no expenses in the expense tracker. Use the command 'add' to create expenses.")
            sys.exit(0)
            return False
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
        if args.amount:
            if args.amount < 0:
                print("Error: the amount for this expense must be a positive value")
                return False
        else:
            return True

    def run(self, expenses, args, file_path):    #checks optional args date/desc/amt and updates expense with provided id
        id = args.id -1
        if args.date:
            expenses[id].update({"date": args.date})
        if args.description:
            expenses[id].update({"description": args.description})
        if args.amount:
            expenses[id].update({"amount": args.amount})
        to_file(expenses, file_path)
        print("Expense updated successfully")
        return
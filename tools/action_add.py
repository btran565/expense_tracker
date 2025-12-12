from tools.utils import to_file, check_date, init_file_path
from tools.action_base import Action

class Add(Action):

    def validate(self, args):
        if args.description == None or args.amount == None:
            print("Error: the action 'add' requires arguments: --date, --description, --amount")
            return False
        if check_date(args.date) == False:
            return False
        if args.amount < 0:
            print("Error: the amount for this expense must be a positive value")
            return False

    def run(self, expenses, args):  #takes list of args and appends it into a dict of dicts. each dict has a int key and dict value
        new_id = len(expenses) + 1
        expenses.append({    #saves date as str in JSON
            "date": args.date, 
            "description": args.description, 
            "amount": args.amount
        })
        
        to_file(expenses, init_file_path())
        print(f"Expense added successfully (ID: {new_id})")
        return 
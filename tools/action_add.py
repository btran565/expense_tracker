from tools.utils import to_file, check_date
from tools.action_base import Action
from datetime import date

class Add(Action):

    def validate(self, args):
        if args.date == None:
            args.date = date.today().strftime("%Y-%m-%d")
        if check_date(args.date) == False:
            return False
        if args.amount < 0:
            print("Error: the amount for this expense must be a positive value")
            return False
        else:
            return True

    def run(self, expenses, args, file_path):  #takes list of args and appends it into a dict of dicts. each dict has a int key and dict value
        new_id = len(expenses) + 1
        expenses.append({    #saves date as str in JSON
            "date": args.date, 
            "description": args.description, 
            "amount": args.amount
        })
        
        to_file(expenses, file_path)
        print(f"Expense added successfully (ID: {new_id})")
        return 
from datetime import datetime
from tools.action_base import Action

class Summary(Action):

    def validate(self, args):
        if args.month:
            if args.month < 1 or args.month > 12:
                print("Error: the 'month' argument must be a valid month from 1 to 12")
                return False
        else:
            return True

    def run(self, expenses, args):
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
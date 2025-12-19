import sys, calendar
from datetime import datetime
from tools.action_base import Action
from tools.utils import expenses_exists

class Summary(Action):

    def validate(self, expenses, args):
        expenses_exists(expenses)
        if args.month:
            if args.month < 1 or args.month > 12:
                print("Error: the 'month' argument must be a valid month from 1 to 12")
                return False
        return True

    def run(self, expenses, args):      #WIP still doesnt account for year
        e_sum = 0   #sum of expenses requested by user
        if args.month:  #if 'month' argument is entered, summary of monthly expense will be printed
            month_name = calendar.month_name[args.month]
            for e in expenses:
                date_obj = datetime.strptime(e['date'], "%Y-%m-%d")
                if date_obj.month == args.month:
                    e_sum += e['amount']
            print(f"Total expenses for {month_name}: ${e_sum}")
            return
        else:
            for e in expenses:
                e_sum += e['amount']
            print(f"Total expenses: ${e_sum}")
        return
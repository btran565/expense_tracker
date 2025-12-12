import sys
from .action_base import Action

class List(Action):
    
    def validate(self):
        return True

    def run(self, expenses):
        if self.validate()==False:
            print("Invalid argument(s). Exiting expense_tracker.py")
            sys.exit(0)
        
        else:
            print(f"{'ID':<3} {'Date':<10} {'Description':<40} {'Amount':<6}")
            for id, e in enumerate(expenses, start=1):
                print(f"{id:<3} {e['date']:<10} {e['description']:<40} {e['amount']:<6}")
            return
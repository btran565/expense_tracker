import sys
from .action_base import Action
from tools.utils import expenses_exists

class List(Action):
    
    def validate(self, expenses):
        expenses_exists(expenses)
        return True

    def run(self, expenses):
        print(f"{'ID':<3} {'Date':<10} {'Description':<40} {'Amount':<6}")
        for id, e in enumerate(expenses, start=1):
            print(f"{id:<3} {e['date']:<10} {e['description']:<40} {e['amount']:<6}")
        return
import sys
from tools.action_base import Action
from tools.utils import to_file, expenses_exists


class Delete(Action):
    
    def validate(self, expenses, args):
        expenses_exists(expenses)
        try:
            id_check = expenses[args.id -1]
        except IndexError:
            print(f"Error: an expense with ID {args.id} does not exist")
            return False
        else:
            return True
    
    def run(self, expenses, args, file_path): #delete expense by popping list
        self.validate(expenses, args)
        del expenses[args.id-1]
        to_file(expenses, file_path)
        print(f"Expense deleted successfully. Use the 'list' action to view updated expense ID's")
        return 
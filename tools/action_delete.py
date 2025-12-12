from tools.action_base import Action
from tools.utils import to_file


class Delete(Action):
    
    def validate(self, expenses, args):
        if args.id == None:
            print("Error: the action 'delete' requires argument: --id")
            return False
        try:
            id_check = expenses[args.id -1]
        except IndexError:
            print(f"Error: an expense with ID {args.id} does not exist")
            return False
    
    def run(self, expenses, args, file_path): #delete expense by popping list
        del expenses[args.id-1]
        to_file(expenses, file_path)
        print(f"Expense deleted successfully. Use the 'list' action to view updated expense ID's")
        return 
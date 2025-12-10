from utils import to_file

def add_data(expenses, args):  #takes list of args and appends it into a dict of dicts. each dict has a int key and dict value
    new_id = len(expenses) + 1
    expenses.append({    #saves date as str in JSON
        "date": args.date, 
        "description": args.description, 
        "amount": args.amount
    })
    
    to_file(expenses)
    print(f"Expense added successfully (ID: {new_id})")
    return 
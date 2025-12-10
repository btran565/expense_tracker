def delete_data(expenses): #delete expense by popping list
    del expenses[args.id-1]
    to_file(expenses)
    print(f"Expense deleted successfully. Use the 'list' action to view updated expense ID's")
    return 
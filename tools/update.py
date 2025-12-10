def update_data(expenses):    #checks optional args date/desc/amt and updates expense with provided id
    id = args.id -1
    if args.date:
        expenses[id].update({"date": args.date})
    if args.description:
        expenses[id].update({"description": args.description})
    if args.amount:
        expenses[id].update({"amount": args.amount})
    to_file(expenses)
    print("Expense updated successfully")
    return
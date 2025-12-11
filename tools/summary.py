def run(expenses):
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
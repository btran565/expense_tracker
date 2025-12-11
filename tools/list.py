

def validate(self):
    pass

def run(expenses):
    print(f"{'ID':<3} {'Date':<10} {'Description':<40} {'Amount':<6}")
    for id, e in enumerate(expenses, start=1):
        print(f"{id:<3} {e['date']:<10} {e['description']:<40} {e['amount']:<6}")
    return
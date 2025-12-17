import sys, os, json
from datetime import datetime

# TODO:  utils method for checking if expense exists
def init_file_path(): #creates and returns file_path
    data_folder = "data"    
    os.makedirs(data_folder, exist_ok=True)

    file_path = os.path.join(data_folder, 'expenses.json')
    if not os.path.exists(file_path):
        # Create an empty expenses.json file if it doesn't exist
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump([], f)    #initialize as empty list ()
    return file_path    #should this be a separate get_path() method?


def to_file(expenses, file_path):  #writes expenses list to json
    with open(file_path, 'w') as f:
        json.dump(expenses, f, indent=4)
    return

def load_expenses(file_path):    #reads json and returns data list
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data

def check_date(date_str):    #changes date string from arg value into date obj
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        print("Date format must be YYYY-MM-DD.")
        return False

def clear_list(expenses, file_path):   #clears expenses list and JSON file
    expenses.clear()
    to_file(expenses, file_path)
    print("List of expenses cleared.")
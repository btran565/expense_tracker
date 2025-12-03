# Expense Tracker CLI Application
Developed using: Python 3.12.3, Linux, CLI, JSON

## About This Project

A small expense tracker that stores expense data in JSON and allows users to complete basic commands such as adding, deleting, and viewing expenses. 

This project was developed in Python 3.12.3 and stores the user's expenses in JSON files. Python's argparse module/library is used to parse the positional and optional arguments given by the user through the Linux CLI to manage their expenses. 

## List of Positional/Optional CLI Arguments:

`add` - Adds an expense with a description, amount, and date (default date set to today's date if not specified). Assigns the expense an ID after its saved.

> `python3 expense_tracker.py add --description 'dinner' --amount '15.36' --date 2025-12-01`


`update` - Uses an existing expense's ID to edit its description, amount, and/or date.

> `python3 expense_tracker.py update --id 2 --amount 25.46`

`delete` - Uses an existing expense's ID to delete it from the tracker.

> `python3 expense_tracker.py delete --id 2`

`list` - Lists the ID's, dates, descriptions, and amounts of all expenses in the tracker.

> `python3 expense_tracker.py list`

`summary` - Displays the sum of all expenses. 

> `python3 expense_tracker.py summary`
> Total expenses: $228.01

If an optional 'month' argument is entered, `summary` will instead display the sum of all expenses for that month.

> 

Working in a Linux environment is new to me, so this expense tracker has helped me get familiar with creating a project that parses command line arguments.

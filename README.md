# Expense Tracker CLI Application
Python 3.12.3, Linux, CLI, JSON

## About This Project

A small expense tracker that stores expense data in JSON and allows users to complete basic commands such as adding, deleting, and viewing expenses. 

This project was developed in Python 3.12.3 and stores the user's expenses in JSON files. Python's argparse module/library is used to parse the positional and optional arguments given by the user through the Linux CLI to manage their expenses. 

## List of positional/optional arguments:
`add` - Adds an expense with a description, amount, and date (default date set to today's date if not specified).

`python3 expense_tracker.py add --description 'dinner' --amount '15.36' --date 2025-12-01`

`python3 expense_tracker.py add --description 'dinner' --amount '15.36'`
(no date specified, so this expense's date will be saved as the current date by default)

`update` - Updates an existing expense's description, amount, and/or date

`delete`

`list`
`summary`

Working in a Linux environment is new to me, so this expense tracker has helped me get familiar with creating a project that parses command line arguments.

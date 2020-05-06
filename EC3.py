#!/usr/bin/env python3

import datetime
import os
import sqlite3
import PySimpleGUI as sg

"""
#    Program calculates and records all personal expenses to a database using a GUI
#    front end. Each expense is stored as a new entry in the database with a
#    timestamp, amount deposited or withdrawn, and a short entry describing the
#    transaction.
"""

db = sqlite3.connect('data/ExpenseSheet.db')

cursor = db.cursor()

# Check if table exists
cursor.execute('''CREATE TABLE IF NOT exists
                  expense(id INTEGER PRIMARY KEY, timestamp TEXT, amount REAL, description TEXT)
''')


"""
Layout of GUI

[            Textfield('amount')  |   Balance('balance')                ]
[            Deposit Radio('deposit') Withdraw Radio('withdraw')        ]
[            Description of Transaction('description') --------->       ]
[ {Submit Button('submit')} {History Button('history')}  {Quit Button}  ]

"""

layout = [
          [sg.InputText(size=(20, 1), key='amount'), sg.VerticalSeparator(), sg.Text(("$ 0"))],
          [sg.Radio('Deposit', "RADIO1", default=False, auto_size_text=True, key='deposit'),
           sg.Radio('Withdraw', "RADIO1", default=False, auto_size_text=True, key='withdraw')],
          [sg.InputText('Description of transaction', size=(45, 5), key='description')],
          [sg.Button('Submit', key='submit'), sg.Button('History', key="history"), sg.Quit()]
         ]

window = sg.Window('Expense Calculator', layout, location=(600, 550), size=(450,150))


def calculate():
    if window.Element('deposit').Get():
        deposit()

    elif window.Element('withdraw').Get():
        withdraw()

    else:
        sg.PopupError("Please select either Deposit or Withdraw", location=(500, 500), no_titlebar=True, line_width=25)

def check_valid_amount(input):
    pass

def check_valid_input(input):
    pass

def deposit():
    amount = window.Element("amount").Get()
    description = window.Element("description").Get()
    is_valid_amount = check_valid_amount(amount)
    is_valid_input = check_valid_input(description)
    curtime = datetime.datetime.now()

    #   loop ensures user enters text for a description
    if is_valid_input is False:
        while is_valid_input is False:
            description = sg.PopupScrolled("Please enter a valid description of the transaction",
                                            size=(50,20),
                                            location=(700, 200))
            is_valid_input = check_valid_input(description)

    #   loop ensures text entered is a number, not a string or a char
    if is_valid_amount is False:
        while is_valid_amount is False:
            transaction = sg.PopupGetText("Please enter a dollar amount into the text field", "",
                                          no_titlebar=True,
                                          location=(600,720))
            is_valid_amount = check_valid_input(amount)

    amount = float(amount)
    curtime = str(curtime)

    try:
        cursor.execute('''INSERT INTO expense(timestamp, amount, description) VALUES(?,?,?)''', (curtime, amount, description))

    except Exception as e:
        db.rollback()
        popup = sg.PopupOK("There was an error. Please retry")

def withdraw():
    pass

# Event loop
while True:
    event, value = window.Read()

    if event == 'submit':
        calculate()

    if event == 'history':
        print_history()

    elif event == 'Quit' or event is None:
        window.Close()
        break

db.close()

import os
import datetime
import tkinter as tk
import openpyxl
from openpyxl import Workbook, load_workbook

###################################################################################################################
#   Program calculates and records all personal expenses in a seperate spreadsheet using a GUI frontend
#   Each expense and piece of data is stored new cells while the balance is a constantly updating cell
#   Every transactions results in a new row on the spreadsheet with:
#    - a timestamp of the time the transaction was entered into GUI
#    - a record of the amount deposited or withdrawn
#    - a description of the transaction
###################################################################################################################

#   Workbook variables
wb = load_workbook('ExpenseSheet.xlsx')
sheet = workbook["Sheet1"]


class App(tk.Frame):
    def __init__(self):
        super.__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
       self.finish = tk.Button(self, text="Finish", command=update_sheet())

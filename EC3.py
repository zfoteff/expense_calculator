import datetime
import os
import python-sql
import PySimpleGUI as sg

layout = [[sg.InputText(size=(20, 1), key='amount'), sg.VerticalSeparator(),
           sg.Text(("$ " + c.select, auto_size_text=True, key='balance')],
          [sg.Radio('Deposit', "RADIO1", default=False, auto_size_text=True, key='deposit'),
           sg.Radio('Withdraw', "RADIO1", default=False, auto_size_text=True, key='withdraw')],
          [sg.InputText('Description of transaction', size=(45, 5), key='description')],
          [sg.Button('Finish', key='finish'), sg.Button('History', key="history"), sg.Quit()]]

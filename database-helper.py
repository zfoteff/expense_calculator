import sqlite3

class DatabaseHelper():
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name".db")
        self.c = self.conn.cursor()
        self.name = db_name

    def create_table(self):
        directive = ('''CREATE TABLE
                       (id integer, name text, date text)''')

        print(directive)

        if self

        self.c.execute(directive)

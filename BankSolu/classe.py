import sqlite3

conn = sqlite3.connect("../data/users.db")

cur = conn.cursor()

class User:

    def __init__(self):
        self.conn = sqlite3.connect("./data/users.db")
        self.conn.row_factory = sqlite3.Row
        self.cur = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cur.execute('''CREATE TABLE IF NOT EXISTS users(
        id INTEGER  PRIMARY KEY,
        nom TEXT,
        prenom INTEGER,
        email TEXT,
        num INTERGER
        )''')

    def add_user(self, nom, prenom, email, num):
        self.cur.execute("""INSERT INTO users(nom, prenom, email, num) VALUES(?, ?, ?, ?)""", (nom, prenom, email, num))
        self.conn.commit()

    def get_all_user(self):
        self.cur.execute('''SELECT * FROM users''')
        users = self.cur.fetchall()
        return users 
     
    def get_user(self):
        pass

    def update(self):
        pass

    def delate(self):
        pass


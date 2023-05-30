import sqlite3


class User:
    def __init__(self):
        self.conn = sqlite3.connect("./users.db")
        self.conn.row_factory = sqlite3.Row
        self.cur = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cur.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                prenom TEXT NOT NULL,
                email TEXT NOT NULL,
                mdp TEXT NOT NULL,
                phone TEXT NOT NULL
            )
        ''')
        self.conn.commit()

    def add_user(self, name, prenom, email, mdp, phone):
        try:
            self.cur.execute('''
                INSERT INTO users(name, prenom, email, mdp, phone)
                VALUES (?, ?, ?, ?, ?)
            ''', (name, prenom, email, mdp, phone))
            self.conn.commit()
            print("User enregistrer")
            return "User enregistrer"
        except Exception as e:
            print(f"Error : {e}")
            return None

    def get_all_users(self):
        self.cur.execute('SELECT * FROM users')
        rows = self.cur.fetchall()

        users = []
        for row in rows:
            user = {
                'id': row['id'],
                'name': row['name'],
                'prenom': row['prenom'],
                'email': row['email'],
                'phone': row['phone']
            }
            users.append(user)

        return users

    def get_user(self, user_id):
        self.cur.execute('SELECT * FROM users WHERE id=?', (user_id,))
        row = self.cur.fetchone()

        if row:
            user = {
                'id': row['id'],
                'name': row['name'],
                'prenom': row['prenom'],
                'email': row['email'],
                'phone': row['phone']
            }
            return user

        return None
    
    def get_user_by_email(self, email):
        self.cur.execute('SELECT * FROM users WHERE email=?', (email,))
        row = self.cur.fetchone()

        if row:
            user = {
                'id': row['id'],
                'name': row['name'],
                'prenom': row['prenom'],
                'email': row['email'],
                'phone': row['phone']
            }
            return user

        return None

    def check_password(self,mdp):
        self.cur.execute('SELECT mdp FROM users')
        rows = self.cur.fetchall()
        mdp = []
        for row in rows:
            mdp.append(row['mdp'])
            return mdp
        return None
    
    def login_user(self, email, password):
        self.cur.execute('SELECT * FROM users WHERE email=? AND mdp=?', (email,password))
        row = self.cur.fetchone()

        if row:
            user = {
                'id': row['id'],
                'name': row['name'],
                'prenom': row['prenom'],
                'email': row['email'],
                'phone': row['phone']
            }
            return user
        return None

    def update_user(self, user_id, new_user):
        self.cur.execute('''
            UPDATE users
            SET name=?, prenom=?, email=?, phone=?
            WHERE id=?
        ''', (new_user['name'], new_user['prenom'], new_user['email'], new_user['phone'], user_id))
        self.conn.commit()

    def delete_user(self, user_id):
        self.cur.execute('DELETE FROM users WHERE id=?', (user_id,))
        self.conn.commit()

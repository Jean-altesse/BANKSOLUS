import sqlite3

conn = sqlite3.connect("./data/users.db")

cur = conn.cursor()

# Classe représentant un utilisateur
class User:
    def __init__(self, name, prenom, email, phone):
        self.name = name
        self.prenom = prenom
        self.email = email
        self.phone = phone

# Classe gérant la base de données des utilisateurs
class UserDatabase:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        
        # Créer la table "users" si elle n'existe pas déjà
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                prenom TEXT NOT NULL,
                email TEXT NOT NULL,
                phone TEXT NOT NULL
            )
        ''')
        self.conn.commit()
    
    def add_user(self, user):
        # Insérer un nouvel utilisateur dans la base de données
        self.cursor.execute('''
            INSERT INTO users (name, prenom, email, phone)
            VALUES (?, ?, ?, ?)
        ''', (user.name, user.prenom, user.email, user.phone))
        self.conn.commit()
    
    def update_user(self, user_id, new_user):
        # Mettre à jour les informations d'un utilisateur dans la base de données
        self.cursor.execute('''
            UPDATE users
            SET name=?, prenom=?, email=?, phone=?
            WHERE id=?
        ''', (new_user.name, new_user.prenom, new_user.email, new_user.phone, user_id))
        self.conn.commit()
    
    def delete_user(self, user_id):
        # Supprimer un utilisateur de la base de données
        self.cursor.execute('DELETE FROM users WHERE id=?', (user_id,))
        self.conn.commit()
    
    def get_all_users(self):
        # Récupérer tous les utilisateurs de la base de données
        self.cursor.execute('SELECT * FROM users')
        rows = self.cursor.fetchall()
        
        users = []
        for row in rows:
            user = User(row[1], row[2], row[3], row[4])
            user.id = row[0]
            users.append(user)
        
        return users

# Exemple d'utilisation
if __name__ == '__main__':
    db = UserDatabase('users.db')
    
    # # Créer un utilisateur
    # user1 = User('John', 'Doe', 'john@example.com', '123456789')
    
    # # Ajouter l'utilisateur à la base de données
    # db.add_user(user1)
    
    # # Récupérer tous les utilisateurs de la base de données
    # all_users = db.get_all_users()
    # for user in all_users:
    #     print(user.name, user.prenom, user.email, user.phone)
    
    # # Mettre à jour les informations d'un utilisateur
    # user1.email = 'new_email@example.com'
    # db.update_user(user1.id, user1)
    
    # # Supprimer un utilisateur
    # db.delete_user(user1.id)
    
    # # Récupérer tous les utilisateurs mis à jour
    # all_users = db.get_all_users()
    # for user in all_users:
    #     print(user.name, user.prenom, user.email, user.phone)

from flask import Flask, render_template, request, redirect
import sqlite3
from users import UserDatabase

app = Flask(__name__)

# Classe gérant la base de données des utilisateurs
class UserDatabase:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        
        # ...

    def verify_credentials(self, email, password):
        # Vérifier les informations d'identification de l'utilisateur dans la base de données
        self.cursor.execute('''
            SELECT * FROM users
            WHERE email=? AND password=?
        ''', (email, password))
        row = self.cursor.fetchone()
        
        if row is None:
            return False
        
        return True

db = UserDatabase('users.db')

# Route pour la page d'accueil
@app.route('/', methods=['GET', 'POST'])
def accueil():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        # Vérifier les informations d'identification dans la base de données
        if db.verify_credentials(email, password):
            # Informations d'identification valides, rediriger vers une autre page
            return redirect('/dashboard')
        
        # Informations d'identification invalides, afficher un message d'erreur
        return render_template('index.html', error=True)
    
    return render_template('index.html', error=False)

# Route pour la page d'inscription
@app.route('/inscription', methods=['GET', 'POST'])
def inscription():
    if request.method == 'POST':
        name = request.form['name']
        prenom = request.form['prenom']
        email = request.form['email']
        phone = request.form['phone']
        
        # Créer un nouvel utilisateur
        user = UserDatabase(name=name, prenom=prenom, email=email, phone=phone)
        
        # Vérifier si l'utilisateur existe déjà dans la base de données
        if not db.user_exists(user):
            # Ajouter l'utilisateur dans la base de données
            db.add_user(user)
            
        # Rediriger vers le tableau de bord
        return redirect('/dashboard')
    
    return render_template('login.html')

# Route pour la connexion de l'utilisateur
@app.route('/connexion', methods=['POST'])
def connexion():
    email = request.form['email']
    password = request.form['password']
    
    # Vérifier les informations d'identification dans la base de données
    if db.verify_credentials(email, password):
        # Informations d'identification valides, rediriger vers le tableau de bord
        return redirect('/dashboard')
    
    # Informations d'identification invalides, afficher un message d'erreur
    return render_template('inscription.html', error=True)

@app.route('/dashboard')
def dashboard():
    # Page du tableau de bord, accessible après une connexion réussie
    return render_template('Tableau_bord.html')

if __name__ == '__main__':
    app.run(debug=True)

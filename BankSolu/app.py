from flask import Flask, render_template, request
<<<<<<< HEAD
=======
from flask_sqlalchemy import SQLAlchemy
>>>>>>> origin/yasmine

app = Flask(__name__)

# Route pour le formulaire d'inscription
@app.route('/', methods=['GET', 'POST'])
def registration():
    if request.method == 'POST':
        name = request.form['name']
        prenom = request.form['prenom']
        email = request.form['email']
        phone = request.form['phone']
        
        # Vérifier si les informations existent dans la base de données users.db
        # Faire la vérification ici
        
        # Si les informations ne sont pas présentes dans la base de données
        if not infos_exist:
            # Effectuer une action (par exemple, afficher un message d'erreur)
            return render_template('verification_failed.html')
        
        # Si les informations existent dans la base de données
        # Effectuer une action (par exemple, rediriger vers une autre page)
        return render_template('verification_success.html')
    
    return render_template('registration.html')

<<<<<<< HEAD
if __name__ == '__main__':
    app.run(debug=True)
=======
@app.route("/index")
def accueil():

    return render_template("index.html")

@app.route("/incription")
def ins():

    return render_template("inscription.html")


@app.route("/trans")
def ls():

    return render_template("transaction_bank.html")



# if __name__ == "__main__":
#     app.run()


# from flask import Flask, render_template, request
# from flask_sqlalchemy import SQLAlchemy


# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///transactions.db'
# db = SQLAlchemy(app)


class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(10), nullable=False)
    montant = db.Column(db.Float, nullable=False)

    def _repr_(self):
        return f"Transaction(type='{self.type}', montant={self.montant})"


@app.route('/')
def transaction():
    solde = Transaction.query.filter_by(type='solde').first()
    depots = Transaction.query.filter_by(type='depot').all()
    retraits = Transaction.query.filter_by(type='retrait').all()
    return render_template('transaction_bank.html', solde=solde, depots=depots, retraits=retraits)


@app.route('/depot', methods=['POST'])
def depot():
    montant = float(request.form['montant'])
    transaction = Transaction(type='depot', montant=montant)
    db.session.add(transaction)
    db.session.commit()
    return 'Success'


@app.route('/retrait', methods=['POST'])
def retrait():
    montant = float(request.form['montant'])
    solde = Transaction.query.filter_by(type='solde').first()
    if montant > solde.montant:
        return 'Solde insuffisant'

    transaction = Transaction(type='retrait', montant=montant)
    db.session.add(transaction)
    db.session.commit()
    return 'Success'


if __name__ == '_main_':
    app.run(debug=True)





















if __name__ == "__main__":
    app.run()
>>>>>>> origin/yasmine

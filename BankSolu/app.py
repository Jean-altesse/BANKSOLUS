from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///projet.db"
db = SQLAlchemy(app)

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
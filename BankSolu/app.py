from flask import Flask, render_template, request, redirect, url_for
from users import User

app = Flask(__name__)

db = User()
# Home page route
@app.route("/", methods=['GET', 'POST'])
def accueil():
    return render_template("index.html")

# Registration route
@app.route('/inscription', methods=['GET', 'POST'])
def inscription():
    if request.method == 'POST':
        name = request.form['name']
        prenom = request.form['prenom']
        email = request.form['email']
        mdp = request.form['mdp']
        phone = request.form['phone']
        user = User()
        try:
            user.add_user(name,prenom,email, mdp,phone)
            print("passs ooo")
        except:
            return render_template("inscription.html", error="Un utilisateur avec cet email existe déjà")
        
        return redirect(url_for('tableau'))
    return render_template('inscription.html')

@app.route('/show_login', methods=['POST', 'GET'])
def show_login():
    return render_template('login.html')


# Login route
@app.route('/connexion', methods=['POST', 'GET'])
def connexion():
    email = request.form['email']
    password = request.form['password']
    
    # Perform login verification here using the User class
    
    return redirect(url_for('index'))

@app.route("/dashboard", methods=['GET', 'POST'])
def tableau():
    return render_template("Tableau_bord.html")

if __name__ == '__main__':
    app.run(debug=True)

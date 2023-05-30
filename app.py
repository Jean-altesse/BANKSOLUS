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
            if not user.get_user_by_email(email):
                user.add_user(name,prenom,email, mdp,phone)
                print("passs ooo")
                return redirect(url_for('connexion'))
            return render_template("inscription.html", error="Un utilisateur avec cet email existe déjà")
        except:
            return render_template("inscription.html", error="Une Erreur s'est produite lors de l'insertion")
        
        
    return render_template('inscription.html')

@app.route('/session', methods=['POST', 'GET'])
def session():
    return render_template('contact.html')

@app.route('/login', methods=['POST', 'GET'])
def show_login():
    return render_template('login.html')

@app.route('/about', methods=['POST', 'GET'])
def about():
    return render_template('apropos.html')


# Login route
@app.route('/connexion', methods=['POST', 'GET'])
def connexion():
    if request.method=="POST":
        email = request.form['email']
        password = request.form['password']
        user=User()
        try:
            if user.login_user(email, password):
                return redirect(url_for('tableau'))
            return render_template('login.html', error="Email ou mot de passe incorrect")
        #     user = db.get_user_by_email(email)
        #     if user:
        #         print("True")
        #         return redirect(url_for('tableau'))
        #     else:
        #         print("False")
        #         return render_template('login.html', error="Email ou mot de passe incorrect")
        except:
            return render_template('login.html', error="Une Erreur s'est produite lors de l'inscription")
    return render_template('login.html')
    # Perform login verification here using the User class
    

@app.route("/dashboard", methods=['GET', 'POST'])
def tableau():
    return render_template("Tableau_bord.html")

if __name__ == '__main__':
    app.run(debug=True)
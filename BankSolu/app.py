from flask import Flask, render_template, request

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

if __name__ == '__main__':
    app.run(debug=True)

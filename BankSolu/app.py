from flask import Flask, render_template, request, redirect, url_for
from classe import User

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get("nom")
        prenom = request.form.get("prenom")
        email = request.form.get("email")
        num = request.form.get("num")
        user = User()
        user.add_student(name, prenom, email, num)
        print(f"nom: {name}, prenom: {prenom}, email: {email}, num: {num}")
        return redirect(url_for("user"))
    return render_template("index.html")

@app.route('/students')
def student():
    user = User()
    data = user.get_all_user()
    for i in data:
        print(i)
    return render_template("list.html", users=user.get_all_user())

@app.route('/students/<int:id>')
def get_user(id):
    return f"""<h2>Je suis l'élève {id}: </h3>"""
from flask import Flask, render_template
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






if __name__ == "__main__":
    app.run()























if __name__ == "__main__":
    app.run()
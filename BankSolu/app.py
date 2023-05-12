from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///projet.db"
db = SQLAlchemy(app)

@app.route("/base.html")
def accueil():

    return render_template("base.html")























if __name__ == "__main__":
    app.run()
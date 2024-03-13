from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/index.html")
def index():
    return render_template("index.html")


@app.route("/connexion.html")
def connexion():
    return render_template("connexion.html")
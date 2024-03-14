from flask import Flask, render_template, request, session

app = Flask(__name__)
app.secret_key = "cmoiwesh"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/index.html", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if not session.get('login'):
            session['login'] = True
        return render_template("index.html")
    return render_template("index.html")


@app.route("/connexion.html")
def connexion():
    return render_template("connexion.html")
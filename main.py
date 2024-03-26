from flask import Flask, render_template, request, session, g
import sqlite3

app = Flask(__name__)
app.secret_key = "cmoiwesh"
DATABASE = "bdd/refuge.db"


def get_db():
    db = getattr(g, "_database", None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    result = cur.fetchall()
    cur.close()
    return (result[0] if result else None) if one else result


def execute_db(query, args=()):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute(query, args)
    conn.commit()
    cursor.close()


def get_chat():
    query = "SELECT * FROM Animal INNER JOIN refuge on animal.idRefuge = refuge.idRefuge LEFT JOIN Login on Login.idLogin = animal.idLogin WHERE espece = ?"
    args = ("chat",)
    return query_db(query, args=args)


def get_chien():
    query = "SELECT * FROM Animal INNER JOIN refuge on animal.idRefuge = refuge.idRefuge LEFT JOIN Login on Login.idLogin = animal.idLogin WHERE espece = ?"
    args = ("chien",)
    return query_db(query, args=args)


def get_elephant():
    query = "SELECT * FROM Animal INNER JOIN refuge on animal.idRefuge = refuge.idRefuge LEFT JOIN Login on Login.idLogin = animal.idLogin WHERE espece = ?"
    args = ("elephant",)
    return query_db(query, args=args)


def get_exotique():
    query = "SELECT * FROM Animal INNER JOIN refuge on animal.idRefuge = refuge.idRefuge LEFT JOIN Login on Login.idLogin = animal.idLogin WHERE espece = ?"
    args = ("exotique",)
    return query_db(query, args=args)


def get_idLogin(mail):
    query = "SELECT idLogin FROM Login WHERE mail = ?"
    args = (mail,)
    return query_db(query, args=args)


def get_mail():
    query = "SELECT mail FROM Login"
    return query_db(query)


def get_password():
    query = "SELECT password FROM Login"
    return query_db(query)


def post_inscription(postMail, postPassword):
    listMail = get_mail()
    test = 0
    for mail in listMail:
        if str(mail[0]) == postMail:
            test = 1
    if test == 1:
        error = "Ce mail est déjà lié à un compte."
        return render_template("inscription.html", error=error)
    else:
        query = "INSERT INTO Login (mail, password) VALUES (?,?)"
        args = (postMail, postPassword)
        try:
            execute_db(query, args=args)
            return render_template("connexion.html")
        except Exception as e:
            error = "Une erreur s'est produite lors de l'inscription."
            print("Erreur lors de l'insertion dans la base de données :", e)
            return render_template("inscription.html", error=error)


def post_connexion(postMail, postPassWord):
    postMail = str(postMail)
    listMail = get_mail()
    listPassword = get_password()
    test = 0
    for mail in listMail:
        for password in listPassword:
            if str(mail[0]) == postMail and str(password[0]) == postPassWord:
                test = 1
    if test == 0:
        error = "Mail ou Mot de passe incorrect"
        return render_template("connexion.html", error=error)
    else:
        if not session.get("login"):
            session["login"] = True
            session["loginMail"] = postMail
        return render_template("index.html")


@app.route("/chat.html")
def chat():
    chats = get_chat()
    return render_template("chat.html", chats=chats)


@app.route("/chien.html")
def chien():
    chiens = get_chien()
    return render_template("chien.html", chiens=chiens)


@app.route("/elephant.html")
def elephant():
    elephants = get_elephant()
    return render_template("elephant.html", elephants=elephants)


@app.route("/exotique.html")
def exotique():
    exotiques = get_exotique()
    return render_template("exotique.html", exotiques=exotiques)


@app.route("/chatReserver.html", methods=["GET", "POST"])
def chatReserver():
    if request.method == "POST":
        idAnimal = request.form["idAnimal"]
        id = get_idLogin(session["loginMail"])
        query = "UPDATE Animal SET idLogin = ?, disponible = 0 WHERE idAnimal = ?"
        args = (id[0][0], idAnimal)
        execute_db(query, args=args)
        chats = get_chat()
        return render_template("/chat.html", chats=chats)


@app.route("/chatDisponible.html", methods=["GET", "POST"])
def chatDereserver():
    if request.method == "POST":
        idAnimal = request.form["idAnimal"]
        print(idAnimal)
        query = "UPDATE Animal SET idLogin = NULL, disponible = 1 WHERE idAnimal = ?;"
        args = idAnimal
        execute_db(query, args=args)
        chats = get_chat()
        return render_template("/chat.html", chats=chats)


@app.route("/chienReserver.html", methods=["GET", "POST"])
def chienReserver():
    if request.method == "POST":
        idAnimal = request.form["idAnimal"]
        id = get_idLogin(session["loginMail"])
        query = "UPDATE Animal SET idLogin = ?, disponible = 0 WHERE idAnimal = ?"
        args = (id[0][0], idAnimal)
        execute_db(query, args=args)
        chiens = get_chien()
        return render_template("/chien.html", chiens=chiens)


@app.route("/chienDisponible.html", methods=["GET", "POST"])
def chienDereserver():
    if request.method == "POST":
        idAnimal = request.form["idAnimal"]
        print(idAnimal)
        query = "UPDATE Animal SET idLogin = NULL, disponible = 1 WHERE idAnimal = ?;"
        args = idAnimal
        execute_db(query, args=args)
        chiens = get_chien()
        return render_template("/chien.html", chiens=chiens)


@app.route("/elephantReserver.html", methods=["GET", "POST"])
def elephantReserver():
    if request.method == "POST":
        idAnimal = request.form["idAnimal"]
        id = get_idLogin(session["loginMail"])
        query = "UPDATE Animal SET idLogin = ?, disponible = 0 WHERE idAnimal = ?"
        args = (id[0][0], idAnimal)
        execute_db(query, args=args)
        elephants = get_elephant()
        return render_template("/elephant.html", elephants=elephants)


@app.route("/elephantDisponible.html", methods=["GET", "POST"])
def elephantDereserver():
    if request.method == "POST":
        idAnimal = request.form["idAnimal"]
        print(idAnimal)
        query = "UPDATE Animal SET idLogin = NULL, disponible = 1 WHERE idAnimal = ?;"
        args = idAnimal
        execute_db(query, args=args)
        elephants = get_elephant()
        return render_template("/elephant.html", elephants=elephants)


@app.route("/exotiqueReserver.html", methods=["GET", "POST"])
def exotiqueReserver():
    if request.method == "POST":
        idAnimal = request.form["idAnimal"]
        id = get_idLogin(session["loginMail"])
        query = "UPDATE Animal SET idLogin = ?, disponible = 0 WHERE idAnimal = ?"
        args = (id[0][0], idAnimal)
        execute_db(query, args=args)
        exotiques = get_exotique()
        return render_template("/exotique.html", exotiques=exotiques)


@app.route("/exotiqueDisponible.html", methods=["GET", "POST"])
def exotiqueDereserver():
    if request.method == "POST":
        idAnimal = request.form["idAnimal"]
        print(idAnimal)
        query = "UPDATE Animal SET idLogin = NULL, disponible = 1 WHERE idAnimal = ?;"
        args = idAnimal
        execute_db(query, args=args)
        exotiques = get_exotique()
        return render_template("/exotique.html", exotiques=exotiques)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/index.html", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        mail = request.form["mail"]
        password = request.form["password"]
        result = post_connexion(mail, password)
        return result
    else:
        return render_template("index.html")


@app.route("/inscription.html")
def inscription():
    return render_template("inscription.html")


@app.route("/connexion.html", methods=["GET", "POST"])
def connexion():
    if request.method == "POST":
        mail = request.form["mail"]
        password = request.form["password"]
        result = post_inscription(mail, password)
        return result
    else:
        return render_template("connexion.html")


@app.route("/deconnexion.html")
def deconnexion():
    session["login"] = False
    session["loginMail"] = ""
    return render_template("index.html")

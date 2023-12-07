from flask import Flask, render_template, request, session, url_for, redirect
import sqlite3
from os.path import join, dirname, realpath

app = Flask(__name__)
app.config['DATA_DIR'] = join(dirname(realpath(__file__)),'static')
app.secret_key = b'99b45274a4b2da7440ab249f17e718688b53b646f3dd57f23a9b29839161749f'

con = sqlite3.connect(join(app.config['DATA_DIR'], "traitement.db"), check_same_thread=False)
cur = con.cursor()

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/connexion")
def login():
    return render_template('login.html')

@app.route("/inscription")
def inscription():
    return render_template('connexion.html')

@app.route("/mon_compte")
def compte():
    session['argent'] = cur.execute("SELECT solde FROM compte WHERE nom=?;", (session['pseudo'],)).fetchone()[0]
    return render_template('compte.html', solde=session['argent'])

@app.route("/retirer")
def retré():
    return render_template('retrait.html')

@app.route("/ajout")
def ajouter():
    return render_template('ajout.html')

@app.route("/retrait", methods=['POST'])
def retrait():
    a = int(request.form['montant'])
    argent = int(cur.execute("SELECT solde FROM compte WHERE nom=?;",(session['pseudo'],)).fetchone()[0])
    montant = argent - a
    cur.execute("UPDATE compte SET solde = ? WHERE nom = ?;", (montant, session['pseudo'],))
    con.commit()
    return render_template('compte.html', solde=montant)

@app.route("/traitement", methods=['POST'])
def maj():
    a = int(request.form['montant'])
    argent = int(cur.execute("SELECT solde FROM compte WHERE nom=?;", (session['pseudo'],)).fetchone()[0])
    montant = a + argent
    cur.execute("UPDATE compte SET solde = ? WHERE nom = ?;", (montant, session['pseudo'],))
    con.commit()
    return render_template('compte.html', solde=montant)

@app.route("/nouveaux", methods=['POST'])
def la_bienvenue():
    session['pseudo'] = request.form['nom']
    if cur.execute("SELECT nom FROM donne WHERE nom=?;", (request.form['nom'],)).fetchone() != None:
        return render_template('connexion.html')
    else:
        cur.execute("INSERT INTO donne(nom, pwd) VALUES(?, ?)", (request.form['nom'], request.form['password'],))
        cur.execute("INSERT INTO coord(mail, nom) VALUES(?, ?)", (request.form['mail'], request.form['nom'],))
        cur.execute("INSERT INTO compte(mail, nom, solde) VALUES(?, ?, ?)", (request.form['mail'], request.form['nom'], 0,))
        con.commit()
    return render_template('bienvenue.html', name=request.form['nom'], ps = session['pseudo'])

@app.route("/greeting", methods=['POST'])
def greeting():
    if cur.execute("SELECT nom FROM donne WHERE nom=? AND pwd=?;", (request.form['nom'], request.form['pwd'],)).fetchone() == None:
        return redirect(url_for("login"))
    if cur.execute("SELECT pwd FROM donne WHERE nom=? AND pwd=?;", (request.form['nom'],request.form['pwd'],)).fetchone() == None:
        return redirect(url_for("login"))
    return render_template('greeting.html', name=request.form['nom'], visibility = True)

app.run(host = '127.0.0.1', port='8080', debug=True, ssl_context='adhoc')
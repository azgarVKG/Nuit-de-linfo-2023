from flask import Flask, render_template, request, session
import sqlite3
from os.path import join, dirname, realpath

app = Flask(__name__)
app.config['DATA_DIR'] = join(dirname(realpath(__file__)),'static')
app.secret_key = b'99b45274a4b2da7440ab249f17e718688b53b646f3dd57f23a9b29839161749f'

con = sqlite3.connect('traitement.db')
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
    solde = cur.execute("SELECT solde FROM compte;").fetchone() 
    session['argent'] = solde
    print(solde)
    return render_template('compte.html', solde=solde, argent = session['argent'])

@app.route("/retirer")
def retré():
    return render_template('retrait.html')

@app.route("/ajout")
def ajouter():
    return render_template('ajout.html')


@app.route("/retrait", methods=['POST'])
def retrait():
    arg = request.form
    a = arg.get('montant')
    argent = cur.execute("SELECT solde FROM compte;") 
    row = cur.fetchall()
    ct = row[0][0]
    new_ct = int(ct)
    new_a = int(a)
    montant = new_ct - new_a
    cur.execute("""UPDATE compte SET solde = ? WHERE nom = ?;""", (montant, session['ps'],))
    con.commit()
    print(session['ps'],argent, new_ct, new_a)
    return render_template('compte.html', solde=montant)






@app.route("/traitement", methods=['POST'])
def maj():
    arg = request.form
    a = arg.get('montant')
    argent = cur.execute("SELECT solde FROM compte;") 
    row = cur.fetchall()
    ct = row[0][0]
    new_ct = int(ct)
    new_a = int(a)
    montant = new_a + new_ct
    cur.execute("""UPDATE compte SET solde = ? WHERE nom = ?;""", (montant, session['ps'],))
    con.commit()
    print(session['ps'],argent, new_ct)
    return render_template('compte.html', solde=montant)

    

@app.route("/nouveaux", methods=['POST'])
def la_bienvenue():
    don = request.form
    ps = don.get('nom')
    session['ps'] = ps
    mdp = don.get('password')
    mail = don.get('mail')
    result = cur.execute("SELECT nom FROM donne WHERE nom=?;", (ps,))
    r = result.fetchall()
    while len(r) == 1:
        return render_template('connexion.html')
    else:
        cur.execute("""INSERT INTO donne(nom, pwd) VALUES(?, ?)""", (ps, mdp,))
        cur.execute("""INSERT INTO coord(mail, nom) VALUES(?, ?)""", (mail, ps,))
        cur.execute("""INSERT INTO compte(mail, nom, solde) VALUES(?, ?, ?)""", (mail, ps, 0,))
        con.commit()
    return render_template('bienvenue.html', name=request.form['nom'], ps = session['ps'])

@app.route("/greeting", methods=['POST'])
def greeting():
    donnees = request.form
    nom = donnees.get('nom')
    pwd = donnees.get('pwd')
    result = cur.execute("SELECT nom FROM donne WHERE nom=?;", (nom,))
    result = cur.fetchall()
    if len(result) == 0:
        ct = result[0][0]
    mdp = cur.execute("SELECT pwd FROM donne WHERE nom=?;", (nom,))
    mdp = cur.fetchall()
    if len(mdp) == 0:
        c = mdp[0][0]
    print(ct, c)
    print(nom, pwd)
    while nom != ct and pwd != c:
        
            return render_template('greeting1.html')
    
    else:
        return render_template('greeting.html', name=request.form['nom'])



app.run(host = '127.0.0.1', port='8080', debug=True)
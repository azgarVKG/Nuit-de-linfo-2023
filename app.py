import uuid
from flask import Flask, render_template, redirect, url_for, request, session

app = Flask(__name__)
app.secret_key = b'6b1c2d979b55431bdc13c133bc026c80311b606aad7f3987b6638970bff1a5e1'

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/game")
def game():
    userID = id = uuid.uuid4()
    return render_template("game.html")
    

if __name__ == "__main__":
    app.run(debug=True)
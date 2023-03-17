# save this as app.py
from flask import Flask
from flask import render_template
from flask import session
import base64
app = Flask(__name__)

@app.route("/")
def start():
    if 'loggedin' in session : 
        return render_template('index.html')
    return render_template('login.html')
    
@app.route("/log", method=["GET", "POST"])
def testlogin():
    with open("data.txt", "r") as fichier:
        for line in fichier:
            datalog = base64.b64decode(line).decode()
    if request.method == "POST" :
        testlog = request.form["login"]+request.form["pwd"]
        session["loggedin"] = True
    return redirect(url_for("start"))

@app.route("/alias")
def alias():
    return render_template('alias.html')
@app.route("/rules_filter")
def rules_filter():
    return render_template('rules_filter.html')
@app.route("/rules_nat")
def rules_nat():
    return render_template('rules_nat.html')
@app.route("/addnat")
def rules_nat_add():
    return render_template('addnat.html')
from flask import Flask
from werkzeug.security import generate_password_hash
from db import Database
from pprint import pprint

app = Flask(__name__)
with app.app_context():  
    db = Database(app)

@app.route('/')
def home() -> str:
    if db.users.insertDB(username="provaDbAbs", password=generate_password_hash("1111"), nome="prova", cognome="prova"):
        print("DAJEEE")
    else:
        print(":()")
    #pprint(dati)
    return "<h1> ciao <h1>"


app.run(debug=True)
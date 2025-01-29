from flask import Flask
from werkzeug.security import generate_password_hash
from db import Database
from pprint import pprint

app = Flask(__name__)
with app.app_context():  
    db = Database(app)

@app.route('/')
def home() -> str:
    #pprint(dati)
    return "<h1> ciao <h1>"



app.run(debug=True)
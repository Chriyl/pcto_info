from flask import Flask
from db import Database
from pprint import pprint

app = Flask(__name__)
with app.app_context():  
    db = Database(app)

@app.route('/')
def home() -> str:
    dati = db.orders.getById(OrderID=10248)
    pprint(dati)
    return "<h1> ciao <h1>"


app.run(debug=True)
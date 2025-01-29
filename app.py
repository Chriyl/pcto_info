from flask import Flask
from werkzeug.security import generate_password_hash
from db import Database
from pprint import pprint
from models import UserModel

app = Flask(__name__)
with app.app_context():  
    db = Database(app)

@app.route('/')
def home() -> str:
    user = UserModel(SupplierName="franco", ContactName="pertini", Address="cicileo" , City="Yeu", PostalCode="72100", Country="italy", phone="3489807675")
    print(user["SupplierName"])
    if db.suppliers.insert(**user):
        print("daje")
    return "<h1> ciao <h1>"



app.run(debug=True)
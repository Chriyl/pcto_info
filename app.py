from flask import Flask
from werkzeug.security import generate_password_hash
from _libs.db import Database
from pprint import pprint
from _libs.models import UserModel

app = Flask(__name__)
with app.app_context():  
    db = Database(app)



@app.route('/')
def home() -> str:
    return "<h1> ciao <h1>"

    

app.run(debug=True)
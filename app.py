from flask import Flask
from db import Database

app = Flask(__name__)
with app.app_context():  # 🔹 Assicura che il database venga inizializzato nel contesto Flask
    db = Database(app)

@app.route('/')
def home() -> str:
    return "<h1> ciao <h1>"


app.run(debug=True)
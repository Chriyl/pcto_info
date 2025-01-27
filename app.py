from flask import Flask

app = Flask(__name__)


@app.route('/')
def home() -> str:
    return "<h1> ciao <h1>"


app.run(debug=True)
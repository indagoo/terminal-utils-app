from app import app
from flask import render_template


@app.route("/")
@app.route("/index")
def index():
    user = {"username": "John Doe"}
    forloop_data = [
        {"name": "asdfasdf", "value": "value1"},
        {"name": "name2", "value": "value2"},
    ]
    return render_template("index.html", title="Home", user=user, forloop=forloop_data, sk = app.secret_key)

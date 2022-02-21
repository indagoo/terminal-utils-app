from flask import flash, redirect, render_template, url_for

from app import app
from app.forms import LoginForm


@app.route("/")
@app.route("/index")
def index():
    user = {"username": "John Doe"}
    forloop_data = [
        {"name": "asdfasdf", "value": "value1"},
        {"name": "name2", "value": "value2"},
    ]
    return render_template("index.html", title="Home", user=user, forloop=forloop_data)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(
            "Logged in as the user {}, remember me = {}".format(
                form.password.data, form.remember_me.data
            )
        )
        return redirect(url_for("index"))
    return render_template("login.html", title="Sign In", form=form)

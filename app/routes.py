from distutils.log import Log
from flask import render_template, flash, redirect, url_for, request
from app import app, db
from app.forms import LoginForm, RegistrationForm
from flask_login import current_user, login_required, login_user, logout_user
from app.models import User
from werkzeug.urls import url_parse


@app.route("/")
@app.route("/index")
@login_required
def index():
    posts = [
        {"author": {"username": "John"}, "body": "Beautiful day in Portland!"},
        {"author": {"username": "Susan"}, "body": "The Avengers movie was so cool!"},
    ]
    return render_template("index.html", title="Home Page", posts=posts)


@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        flash("You are already logged in as {}".format(current_user.username)) # can remove
        return redirect(url_for("index"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash("Invalid user or password!")
            return redirect(url_for("login"))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            flash("Successfully logged in as {}".format(user.username)) #can remove
            return redirect(url_for("index"))
        return redirect(next_page)
    return render_template("login.html", form=form, title="Sign In")


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("index"))

@app.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        flash("You are already logged in as {}".format(current_user.username)) # can remove
        return redirect(url_for("index"))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("Congratulations on successful registration!")
        return redirect(url_for("login"))
    return render_template("register.html",form=form,title="Register")

@app.route("/user/<username>")
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    posts = [
        {'author': user, 'body': 'Test Post 1'},
        {'author': user, 'body': 'Test Post 2'}
    ]
    return render_template("user.html", user=user, posts=posts)
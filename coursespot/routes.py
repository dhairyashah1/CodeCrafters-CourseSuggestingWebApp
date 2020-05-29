from flask import render_template, redirect, url_for, flash, request
from coursespot import app, db, bcrypt
from coursespot.forms import RegistrationForm, LoginForm
from coursespot.models import User


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_pw = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(
            firstname = form.firstname.data,
            lastname = form.lastname.data,
            username = form.username.data,
            email = form.email.data,
            password = hashed_pw
        )
        db.session.add(user)
        db.session.commit()
        flash("Account created successfully. You can now login", "success")
        return redirect(url_for('login'))
    return render_template('register.html', title="Register", form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            flash("Login successful", "success")
            return redirect(url_for('home'))
        else:
            flash("Login unsuccessful. Please check your email and password", "danger")
    return render_template('login.html', title="Login", form=form)  

@app.route("/about")
def about():
    return render_template("about.html", title="About")

@app.route("/help")
def help():
    return render_template("help.html", title="Help")
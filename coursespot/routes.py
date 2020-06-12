from flask import render_template, redirect, url_for, flash, request
from coursespot import app, db, bcrypt
from coursespot.forms import RegistrationForm, LoginForm, ContactForm
from coursespot.models import User, Contact
from flask_login import login_user, current_user, logout_user, login_required


@app.route("/")
def welcome():
    return render_template("welcome.html", title="Welcome")



@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
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
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash("Login unsuccessful. Please check your email and password", "danger")
    return render_template('login.html', title="Login", form=form)  


@app.route("/about")
def about():
    return render_template("about.html", title="About")

@app.route("/help")
def help():
    return render_template("help.html", title="Help")

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route("/account")
@login_required
def account():
    return render_template("account.html", title="Account")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    form = ContactForm()
    contact = Contact(email = form.email.data, message = form.message.data)
    db.session.add(contact)
    db.session.commit()
    return render_template("contact.html", form=form, title="Contact")
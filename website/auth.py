from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db


auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if User:
            if check_password_hash(user.password, password):
                flash('logged in successfully!', category='success')
            else:
                flash('Incorrect Password, Try again', category='error')
        else:
            flash('Email does not exist', category='error')

    return render_template("/login.html", boolean=True)


@auth.route('/logout')
def logout():
    return "<p>logout</p>"


@auth.route('/sign-up', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        fname = request.form.get('fname')
        lname = request.form.get('lname')
        pass1 = request.form.get('pass1')
        pass2 = request.form.get('pass2')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('email already exists', category="error")
        elif len(email) < 4:
            flash('Enter email correctly', category='error')
            pass
        elif len(fname) < 2:
            flash('Invalid Name', category='error')
            pass
        elif len(lname) < 2:
            flash('Invalid Name', category='error')
            pass
        elif len(pass1) < 7:
            flash('password must have 8 characters', category='error')
            pass
        elif len(pass1) != len(pass2):
            flash('password did not match', category='error')
            pass

        else:
            new_user = User(email=email, fname=fname, password= generate_password_hash(pass1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()

            flash('account created', category='success')
            return redirect(url_for('views.home'))

    return render_template("sign-up.html", boolean=True)
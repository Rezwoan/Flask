from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form
    print(data)
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

        if len(email) < 4:
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
            flash('account created', category='success')
            #add user

    return render_template("sign-up.html", boolean=True)